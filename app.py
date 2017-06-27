from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# items = session.query(MenuItem).filter_by(name="Veggie Burger")
# for item in items:
#     print(str(item.id) + " " + item.price + " " + item.restaurant.name)

items = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
print(items)
# for item in items:
#     print(str(item.id) + " " + item.price + " " + item.restaurant.name)
#     if item.id == 44:
#         session.delete(item)
#         session.commit()
# item.price = '$2.99'
# session.add(item)
# session.commit()
