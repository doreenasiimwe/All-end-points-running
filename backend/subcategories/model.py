from backend.db import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SubCategory(db.Model):
    __tablename__ = "sub_categories"
    name:str
    
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),unique=True)
    created_by  = db.Column(db.Integer,db.ForeignKey('users.id'))
    created_at = db.Column(db.String(255),nullable=True,default=datetime.now())
    updated_at = db.Column(db.String(255),nullable=True,onupdate=datetime.now())
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    fooditems = db.relationship("FoodItem", backref='sub_category', remote_side=[id], lazy='dynamic')
    
   

    def __init__(self,name,created_by,category_id):
     
     self.name = name
     self.created_by = created_by
     self.category_id = category_id
    #  self.created_at = created_at
    #  self.updated_at = updated_at
     
    

    def __repr__(self):
        return f"<SubCategory {self.name} >"
