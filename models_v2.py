import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.filemanager import ImageManager
from flask import Markup, url_for

class selling record(Model):
    id = Column(Integer, primary_key)
    item_id = Column(Integer,ForeignKey('item_id'),nullable=False)
    item = relationship("item")
    End_date = Column(Date, nullable=False)
    FirstPrice = Column(Integer,nullable=False)
    FinalPrice = Column(Integer,nullable=False)
    'SellerUser_id = Column(Integer,nullable=False)
