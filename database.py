import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
db_string = "mysql+pymysql://csupqj8pv97jqs61vmv4:pscale_pw_Fkyc2aOFQIo2Ev8S04gnfyUj2jZtXDiGs54G8uKXWQM@aws.connect.psdb.cloud/trackery?charset=utf8mb4"

engine = create_engine("mysql+pymysql://csupqj8pv97jqs61vmv4:pscale_pw_Fkyc2aOFQIo2Ev8S04gnfyUj2jZtXDiGs54G8uKXWQM@aws.connect.psdb.cloud/trackery?charset=utf8mb4", 
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    })




