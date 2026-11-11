from db import engine, SessionLocal, Base
import models 


def main():
    Base.metadata.create_all(engine)

    return



if __name__ == "main":
    main()
