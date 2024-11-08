# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///euro-academy.db'  # Use SQLite or your preferred DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
