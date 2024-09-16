import argparse
from database import database, client
from models.Company import Company
from models.Trainee import Trainee
from models.Transaction import Transaction

# Create the parser
parser = argparse.ArgumentParser(description='create or drop collections.')

# Add the arguments
parser.add_argument('direction', metavar='U', type=str,
                    help='up => create collections, down => drop collections')

# Parse the arguments
args = parser.parse_args()
direction = args.direction

if direction not in ['up', 'down', 'update']:
    raise Exception("Invalid argument: ", args)


def up(db_models):
    for model in db_models:
        try:
            model.up()

            print('Successfully created: ', model.describe())
        except Exception as up_error:
            print(f'Unable to create {model.describe()} due to the following error: ', up_error)


def update(db_models):
    for model in db_models:
        try:
            model.update()

            print('Successfully updated: ', model.describe())
        except Exception as down_error:
            print(f"Unable to update {model.describe()} due to the following error: ", down_error)


def down(db_models):
    for model in db_models:
        try:
            model.down()

            print('Successfully dropped: ', model.describe())
        except Exception as down_error:
            print(f"Unable to drop {model.describe()} due to the following error: ", down_error)


try:
    create_models = [Company(database), Trainee(database), Transaction(database)]
    update_models = [Company(database), Trainee(database), Transaction(database)]
    drop_models = [Trainee(database), Company(database), Transaction(database)]

    if direction == 'up':
        up(create_models)
    elif direction == 'down':
        down(drop_models)
    else:
        update(update_models)

    client.close()
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
