from peewee import *
import pathlib

path = pathlib.Path('eduquest.sqlite')
conn = SqliteDatabase('eduquest.sqlite')


class BaseModel(Model):
    class Meta:
        database = conn


class Hero(BaseModel):
    hero_id = AutoField(column_name='HeroId')
    hero_name = TextField(column_name='Name', null=True)
    hero_race = TextField(column_name='Race', null=True)
    hero_class = TextField(column_name='Class', null=True)
    hero_age = IntegerField(column_name='Age', null=True)

    class Meta:
        table_name = 'Heroes'


def print_last_five_artists():
    """ Печатаем последние 5 записей в таблице исполнителей"""
    print('########################################################')
    cur_query = Hero.select().limit(5).order_by(Hero.hero_id.desc())
    for item in cur_query.dicts().execute():
        print('hero: ', item)


# create table
def create_tables():
    with conn:
        conn.create_tables([Hero])


if not path.exists():
    create_tables()

# Создаем курсор - это специальный объект который делает запросы
# и получает их результаты
cursor = conn.cursor()

# cursor.execute("SELECT Name FROM Heroes ORDER BY Name LIMIT 3")
# results = cursor.fetchall()
# print(results)
#
# hero = Hero.get(Hero.hero_id == 1)
# print('hero: ', hero.hero_id, hero.hero_name)
#
# #  request example
# query = Hero.select()
# print(query)
# query = Hero.select().where(Hero.hero_id < 10). \
#     limit(5).order_by(Hero.hero_id.desc())
# print(query)
#
# hero_selected = query.dicts().execute()
# print(hero_selected)
# for hero in hero_selected:
#     print('hero: ', hero)
#
# # create
# 1
Hero.create(hero_name='Test1', hero_race='Test1', hero_class='Test1', hero_age=10)
# 2
hero = Hero(hero_name='Test2', hero_race='Test2', hero_class='Test2', hero_age=10)
hero.save()
# 3
hero_data = [{'hero_name': 'Test3', 'hero_race': 'Test3', 'hero_class': 'Test3', 'hero_age': 10},
             {'hero_name': 'Test4', 'hero_race': 'Test4', 'hero_class': 'Test4', 'hero_age': 10}]
Hero.insert_many(hero_data).execute()

print_last_five_artists()
#
# # update
# hero = Hero(hero_name='Test2!', hero_race='Test2!', hero_class='Test2!', hero_age=10)
# hero.hero_id = 277  # первичный ключ
# hero.save()
#
# print_last_five_artists()
#
# # many
# query = Hero.update(name=Hero.name + '!!!').where(Hero.artist_id > 275)
# query.execute()
#
# print_last_five_artists()
#
# # delete
#
# hero = Hero.get(Hero.hero_id == 279)
# hero.delete_instance()
#
# print_last_five_artists()
#
# # delete many
# query = Hero.delete().where(Hero.hero_id > 275)
# query.execute()
