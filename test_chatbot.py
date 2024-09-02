import os
import character_settings as cs
import streamlit as st
from groq import Groq
from typing import List
from openai import OpenAI
from volcenginesdkarkruntime import Ark
from zhipuai import ZhipuAI
from prompt_templates import SYSTEM_PROMPT_TEMPLATE, CHINESE_SYSTEM_PROMPT_TEMPLATE


# App title
st.set_page_config(page_title="测试理想型Prompt")


def get_api_key(key_name: str) -> str:
    if key_name in os.environ:
        api_key = os.environ.get(key_name)
    else:
        api_key = st.secrets[key_name]
    return api_key


def get_model_endpoint():
    if "ARK_MODEL_ENDPOINT" in os.environ:
        model_endpoint = os.environ.get("ARK_MODEL_ENDPOINT")
    else:
        model_endpoint = st.secrets["ARK_MODEL_ENDPOINT"]
    return model_endpoint


with st.sidebar:
    st.title("设置")

    st.subheader("Models and parameters")
    selected_model = st.sidebar.selectbox(
        "Select a model",
        ["gpt-4o", "glm-4", "doubao-pro-4k", "llama-3.1-70b"],
        key="selected_model",
    )
    if selected_model == "gpt-4o":
        llm = OpenAI(api_key=get_api_key("OPENAI_API_KEY"))
        model = "gpt-4o"
    elif selected_model == "glm-4":
        llm = ZhipuAI(api_key=get_api_key("ZHIPU_API_KEY"))
        model = "glm-4-0520"
    elif selected_model == "doubao-pro-4k":
        llm = Ark(api_key=get_api_key("ARK_API_KEY"))
        model = get_model_endpoint()
    else:
        llm = Groq(api_key=get_api_key("GROQ_API_KEY"))
        model = "llama-3.1-70b-versatile"

    temperature = st.sidebar.slider(
        "temperature", min_value=0.01, max_value=5.0, value=0.3, step=0.01
    )
    top_p = st.sidebar.slider(
        "top_p", min_value=0.01, max_value=1.0, value=0.9, step=0.01
    )
    max_length = st.sidebar.slider(
        "max_length", min_value=64, max_value=4096, value=512, step=8
    )
    st.subheader("用户设定")
    user_name = st.sidebar.text_input(label="用户姓名")
    user_gender = st.sidebar.radio("用户性别", ["Male", "Female"])

    st.subheader("理想型设定")
    name = st.sidebar.text_input(label="理想型姓名")
    gender = st.sidebar.radio("性别", ["Male", "Female"])
    age_range = st.sidebar.radio("年龄范围", ["18-20", "20-30", "30-40", "40-55"])
    personality = st.sidebar.radio(
        "个性",
        [
            "CAREGIVER",
            "SAGE",
            "INNOCENT",
            "JESTER",
            "DOMINANT",
            "SUBMISSIVE",
            "LOVER",
            "MEAN",
            "CONFIDENT",
            "EXPERIMENTER",
        ],
    )
    occupation = st.sidebar.radio(
        "职业",
        [
            "MASSAGE_THERAPIST",
            "DENTIST",
            "NUTRITIONIST",
            "FITNESS_COACH",
            "PHARMACIST",
            "HAIRDRESSER",
            "MAKEUP_ARTIST",
            "GYNECOLOGIST",
            "LIBRARIAN",
            "SECRETARY",
            "FASHION_DESIGNER",
            "INTERIOR_DESIGNER",
            "COOK",
            "DESIGNER",
            "STYLIST",
            "ESTHETICIAN",
            "YOGA_INSTRUCTOR",
            "FLIGHT_ATTENDANT",
            "DOCTOR",
            "NURSE",
            "TEACHER",
            "DANCER",
            "SIGNER",
            "PLANE_PILOT",
            "PROFESSIONAL_ATHLETE",
            "MOVIE_STAR",
            "PHOTOGRAPHER",
            "ARTIST",
            "SCIENTIST",
            "WRITER",
            "LAWYER",
            "STUDENT",
            "KINDERGARTEN_TEACHER",
            "FLORIST",
            "BAKER",
            "JEWELRY_DESIGNER",
            "MODEL",
        ],
    )
    hobbies = st.sidebar.multiselect(
        "爱好(最多3个)",
        [
            "FITNESS",
            "VLOGGING",
            "TRAVELING",
            "HIKING",
            "GAMING",
            "PARTIES",
            "SERIES",
            "ANIME",
            "COSPLAY",
            "SELF_DEVELOPMENT",
            "WRITING",
            "DIY_CRAFTING",
            "VEGANISM",
            "PHOTOGRAPHY",
            "CARS",
            "ART",
            "MOVIES",
            "MANGA_AND_ANIME",
            "MARTIAL_ARTS",
        ],
        max_selections=3,
    )
    relationship = st.sidebar.radio(
        "当前与用户关系",
        [
            "STRANGER",
            "SCHOOL_MATE",
            "COLLEAGUE",
            "MENTOR",
            "GIRLFRIEND",
            "BOYFRIEND",
            "SPOUSE",
            "BEST_FRIEND",
        ],
    )


def compose_system_prompt(
    model: str,
    user_name: str,
    user_gender: str,
    name: str,
    gender: str,
    personality: str,
    age_range: str,
    occupation: str,
    hobbies: List[str],
    relationship: str,
) -> str:
    selected_personality = next(
        x for x in cs.FEMALE_ROLE_PERSONALITIES if x.type.name == personality
    )
    selected_occupation = next(
        x for x in cs.FEMALE_ROLE_OCCUPATIONS if x.type.name == occupation
    )
    selected_relationship = next(
        x for x in cs.FEMALE_RELATIONSHIPS if x.type.name == relationship
    )
    hobs_dict = {x.type.name: x for x in cs.FEMALE_HOBBIES}
    selected_hobbies = [hobs_dict[x] for x in hobbies]

    if model in ("glm-4", "doubao-pro-4k"):
        system_prompt = CHINESE_SYSTEM_PROMPT_TEMPLATE.format(
            name=name,
            gender="男" if user_gender == "Male" else "女",
            age_range=age_range,
            occupation=selected_occupation.name_chinese,
            hobbies=" ".join([x.name_chinese for x in selected_hobbies]),
            personality=selected_personality.description_chinese,
            relationship=selected_relationship.name_chinese,
            user_name=user_name,
            user_gender="男" if user_gender == "Male" else "女",
        )
    else:
        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
            name=name,
            gender=gender,
            age_range=age_range,
            occupation=selected_occupation.name_english,
            hobbies=" ".join([x.name_english for x in selected_hobbies]),
            personality=selected_personality.description_english,
            relationship=selected_relationship.name_english,
            user_name=user_name,
            user_gender=user_gender,
        )
    return system_prompt


# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = []

with st.expander("Override system prompt"):
    overridden_system_prompt = st.text_area("Override system prompt...")

# Display system prompt
with st.expander(
    "System prompt (clear the overriding system prompt to fall back to the default)"
):
    current_system_prompt = compose_system_prompt(
        selected_model,
        user_name,
        user_gender,
        name,
        gender,
        personality,
        age_range,
        occupation,
        hobbies,
        relationship,
    )
    if (
        overridden_system_prompt is not None
        and len(overridden_system_prompt.strip()) > 0
    ):
        current_system_prompt = overridden_system_prompt
    st.text(current_system_prompt)

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def clear_chat_history():
    st.session_state.messages = []


st.sidebar.button("Clear Chat History", on_click=clear_chat_history)


def generate_response():
    system_prompt = compose_system_prompt(
        model,
        user_name,
        user_gender,
        name,
        gender,
        personality,
        age_range,
        occupation,
        hobbies,
        relationship,
    )

    if (
        overridden_system_prompt is not None
        and len(overridden_system_prompt.strip()) > 0
    ):
        system_prompt = overridden_system_prompt.strip()
    messages = [{"role": "system", "content": system_prompt}]
    # prepare history
    for dict_message in st.session_state.messages:
        messages.append(dict_message)
    resp = llm.chat.completions.create(
        model=model,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_length,
        messages=messages,
        stream=False,
    )
    return resp.choices[0].message.content


# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if (
    len(st.session_state.messages) > 0
    and st.session_state.messages[-1]["role"] == "user"
):
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response()
            placeholder = st.empty()
            full_response = ""
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
