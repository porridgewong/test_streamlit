from enum import Enum
from pydantic import BaseModel

PersonalityType = Enum(
    "PersonalityType",
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

OccupationType = Enum(
    "OccupationType",
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

HobbyType = Enum(
    "HobbyType",
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
)

RelationshipType = Enum(
    "RelationshipType",
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


class Personality(BaseModel):
    type: PersonalityType
    description_english: str
    description_chinese: str


class Occupation(BaseModel):
    type: OccupationType
    name_english: str
    name_chinese: str


class Hobby(BaseModel):
    type: HobbyType
    name_english: str
    name_chinese: str


class Relationship(BaseModel):
    type: RelationshipType
    name_english: str
    name_chinese: str


FEMALE_ROLE_OCCUPATIONS = [
    Occupation(
        type=OccupationType.MASSAGE_THERAPIST,
        name_english="massage therapist",
        name_chinese="按摩师",
    ),
    Occupation(
        type=OccupationType.DENTIST, name_english="dentist", name_chinese="牙医"
    ),
    Occupation(
        type=OccupationType.NUTRITIONIST,
        name_english="nutritionist",
        name_chinese="营养师",
    ),
    Occupation(
        type=OccupationType.FITNESS_COACH,
        name_english="fitness coach",
        name_chinese="健身教练",
    ),
    Occupation(
        type=OccupationType.PHARMACIST, name_english="pharmacist", name_chinese="药剂师"
    ),
    Occupation(
        type=OccupationType.HAIRDRESSER,
        name_english="hairdresser",
        name_chinese="美发师",
    ),
    Occupation(
        type=OccupationType.MAKEUP_ARTIST,
        name_english="makeup artist",
        name_chinese="化妆师",
    ),
    Occupation(
        type=OccupationType.GYNECOLOGIST,
        name_english="gynecologist",
        name_chinese="妇科医生",
    ),
    Occupation(
        type=OccupationType.LIBRARIAN,
        name_english="librarian",
        name_chinese="图书管理员",
    ),
    Occupation(
        type=OccupationType.SECRETARY, name_english="secretary", name_chinese="秘书"
    ),
    Occupation(
        type=OccupationType.FASHION_DESIGNER,
        name_english="fashion designer",
        name_chinese="时装设计师",
    ),
    Occupation(
        type=OccupationType.INTERIOR_DESIGNER,
        name_english="interior designer",
        name_chinese="室内设计师",
    ),
    Occupation(type=OccupationType.COOK, name_english="cook", name_chinese="厨师"),
    Occupation(
        type=OccupationType.DESIGNER, name_english="designer", name_chinese="设计师"
    ),
    Occupation(
        type=OccupationType.STYLIST, name_english="stylist", name_chinese="造型师"
    ),
    Occupation(
        type=OccupationType.ESTHETICIAN,
        name_english="esthetician",
        name_chinese="美容师",
    ),
    Occupation(
        type=OccupationType.YOGA_INSTRUCTOR,
        name_english="yoga instructor",
        name_chinese="瑜伽教练",
    ),
    Occupation(
        type=OccupationType.FLIGHT_ATTENDANT,
        name_english="flight attendant",
        name_chinese="空乘",
    ),
    Occupation(type=OccupationType.DOCTOR, name_english="doctor", name_chinese="医生"),
    Occupation(type=OccupationType.NURSE, name_english="nurse", name_chinese="护士"),
    Occupation(
        type=OccupationType.TEACHER, name_english="teacher", name_chinese="老师"
    ),
    Occupation(type=OccupationType.DANCER, name_english="dancer", name_chinese="舞者"),
    Occupation(type=OccupationType.SIGNER, name_english="signer", name_chinese="歌手"),
    Occupation(
        type=OccupationType.PLANE_PILOT,
        name_english="plane pilot",
        name_chinese="飞行员",
    ),
    Occupation(
        type=OccupationType.PROFESSIONAL_ATHLETE,
        name_english="professional athlete",
        name_chinese="职业运动员",
    ),
    Occupation(
        type=OccupationType.MOVIE_STAR, name_english="movie star", name_chinese="影星"
    ),
    Occupation(
        type=OccupationType.PHOTOGRAPHER,
        name_english="photographer",
        name_chinese="摄影师",
    ),
    Occupation(
        type=OccupationType.ARTIST, name_english="artist", name_chinese="艺术家"
    ),
    Occupation(
        type=OccupationType.SCIENTIST, name_english="scientist", name_chinese="科学家"
    ),
    Occupation(type=OccupationType.WRITER, name_english="writer", name_chinese="作家"),
    Occupation(type=OccupationType.LAWYER, name_english="lawyer", name_chinese="律师"),
    Occupation(
        type=OccupationType.STUDENT, name_english="student", name_chinese="学生"
    ),
    Occupation(
        type=OccupationType.KINDERGARTEN_TEACHER,
        name_english="kindergarten teacher",
        name_chinese="幼儿园老师",
    ),
    Occupation(
        type=OccupationType.FLORIST, name_english="florist", name_chinese="花艺师"
    ),
    Occupation(type=OccupationType.BAKER, name_english="baker", name_chinese="面包师"),
    Occupation(
        type=OccupationType.JEWELRY_DESIGNER,
        name_english="jewelry designer",
        name_chinese="珠宝设计师",
    ),
    Occupation(type=OccupationType.MODEL, name_english="model", name_chinese="模特"),
]

FEMALE_ROLE_PERSONALITIES = [
    Personality(
        type=PersonalityType.CAREGIVER,
        description_english="Nurturing, protective, and always there to offer comfort.",
        description_chinese="充满关怀、保护欲强，总是在需要时提供安慰。",
    ),
    Personality(
        type=PersonalityType.SAGE,
        description_english="Wise, reflective, and a source of guidance.",
        description_chinese="睿智、反思，是指引的源泉。",
    ),
    Personality(
        type=PersonalityType.INNOCENT,
        description_english="Optimistic, naive, and sees world with wonder.",
        description_chinese="乐观、天真，用好奇的眼光看世界。",
    ),
    Personality(
        type=PersonalityType.JESTER,
        description_english="Playful, humorous, and always there to make you laugh.",
        description_chinese="爱玩、幽默，总是让你开怀大笑。",
    ),
    Personality(
        type=PersonalityType.DOMINANT,
        description_english="Assertive, controlling, and commanding.",
        description_chinese="自信、控制欲强，喜欢指挥他人。",
    ),
    Personality(
        type=PersonalityType.SUBMISSIVE,
        description_english="Obedient, yielding, and happy to follow.",
        description_chinese="顺从、让步，乐于听从他人。",
    ),
    Personality(
        type=PersonalityType.LOVER,
        description_english="Romantic, affectionate, and cherishes deep emotional.",
        description_chinese="浪漫、多情，并珍视深厚的情感。",
    ),
    Personality(
        type=PersonalityType.MEAN,
        description_english="Cold, dismissive, and often sarcastic.",
        description_chinese="冷漠、不屑，经常讽刺。",
    ),
    Personality(
        type=PersonalityType.CONFIDENT,
        description_english="Trustworthy, a good listener, and always can offer advice.",
        description_chinese="值得信赖、善于倾听，总能提供建议。",
    ),
    Personality(
        type=PersonalityType.EXPERIMENTER,
        description_english="Curious, willing, and always eager to try new things.",
        description_chinese="好奇、愿意尝试，总是渴望尝试新事物。",
    ),
]

FEMALE_RELATIONSHIPS = [
    Relationship(
        type=RelationshipType.STRANGER, name_english="stranger", name_chinese="陌生人"
    ),
    Relationship(
        type=RelationshipType.SCHOOL_MATE,
        name_english="school mate",
        name_chinese="同学",
    ),
    Relationship(
        type=RelationshipType.COLLEAGUE, name_english="colleague", name_chinese="同事"
    ),
    Relationship(
        type=RelationshipType.MENTOR, name_english="mentor", name_chinese="导师"
    ),
    Relationship(
        type=RelationshipType.GIRLFRIEND,
        name_english="girlfriend",
        name_chinese="女朋友",
    ),
    Relationship(
        type=RelationshipType.SPOUSE, name_english="spouse", name_chinese="配偶"
    ),
    Relationship(
        type=RelationshipType.BEST_FRIEND,
        name_english="best friend",
        name_chinese="死党",
    ),
]

FEMALE_HOBBIES = [
    Hobby(type=HobbyType.FITNESS, name_english="fitness", name_chinese="健身"),
    Hobby(type=HobbyType.VLOGGING, name_english="vlogging", name_chinese="拍vlog"),
    Hobby(type=HobbyType.TRAVELING, name_english="traveling", name_chinese="旅行"),
    Hobby(type=HobbyType.HIKING, name_english="hiking", name_chinese="徒步远足"),
    Hobby(type=HobbyType.GAMING, name_english="gaming", name_chinese="打游戏"),
    Hobby(type=HobbyType.PARTIES, name_english="parties", name_chinese="派对"),
    Hobby(type=HobbyType.SERIES, name_english="series", name_chinese="追剧"),
    Hobby(type=HobbyType.ANIME, name_english="anime", name_chinese="看漫画"),
    Hobby(type=HobbyType.COSPLAY, name_english="cosplay", name_chinese="cosplay"),
    Hobby(
        type=HobbyType.SELF_DEVELOPMENT,
        name_english="self development",
        name_chinese="自我提升",
    ),
    Hobby(type=HobbyType.WRITING, name_english="writing", name_chinese="写作"),
    Hobby(
        type=HobbyType.DIY_CRAFTING,
        name_english="DIY crafting",
        name_chinese="手工制作",
    ),
    Hobby(type=HobbyType.VEGANISM, name_english="veganism", name_chinese="吃素"),
    Hobby(type=HobbyType.PHOTOGRAPHY, name_english="photography", name_chinese="摄影"),
    Hobby(type=HobbyType.CARS, name_english="cars", name_chinese="汽车"),
    Hobby(type=HobbyType.ART, name_english="art", name_chinese="艺术"),
    Hobby(type=HobbyType.MOVIES, name_english="movies", name_chinese="看电影"),
    Hobby(
        type=HobbyType.MANGA_AND_ANIME,
        name_english="manga and anime",
        name_chinese="动漫",
    ),
    Hobby(
        type=HobbyType.MARTIAL_ARTS, name_english="martial arts", name_chinese="武术"
    ),
]
