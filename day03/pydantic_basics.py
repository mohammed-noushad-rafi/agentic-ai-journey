# from dataclasses import dataclass

# @dataclass
# class User:
#     name: str
#     age: int

# u = User(name="Rafi", age="not a number")
# print(u)    # no error! The bad data gets in silently
from pydantic import BaseModel,ValidationError,Field

class user(BaseModel):
    name:str =Field(max_length=15)
    age:int=Field(le=50)

# u=user(name="noushad",age=22)
# print(u)
# print(u.name)
# u2=user(name="noushad",age="23")
# print(u2.age)
# try:
#     user(name="genai",age="3days")
# except ValidationError as e:
#     print (f"errorrr{e}")
# class Address(BaseModel):
#     city: str
#     dic: str
# class user(BaseModel):
#     name:str 
#     age:int 
#     skills:list[str]=[]
#     goal:str="GenAi Engineer"
#     email: str | None = None   
#     address: Address               

# s=user(
#     name="noushad",age=23,
#     skills=["AI and Ml","Claude"],address={"city":"kushalnagar","dic":"kodagu",}
# )    
# print(s.address.city,s.name,s.email,s.skills)
# data = {"name": "Rafi", "skills": ["python"], 
#         "address": {"city": "Madikeri", "district": "Kodagu"}}
# s1=user.model_validate(data)
# text = '{"name": "Ali", "address": {"city": "Mysuru", "district": "Mysuru"}}'
# s2 = user.model_validate_json(text)
# print(s1.model_dump())
# print(s2.model_dump_json(indent=2))
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)            
    stock: int = Field(ge=0, default=0)   

Product(name="Pen", price=10)   