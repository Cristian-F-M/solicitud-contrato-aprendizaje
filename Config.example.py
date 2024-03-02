class Config:
    # TODO Add the url to your database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@127.0.0.1:3306/%{databasename}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
