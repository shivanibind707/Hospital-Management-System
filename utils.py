def get_positive_int(massage):

        while True:

            try:
                value=int(input(massage))
                if value<=0:
                    print("Number Must Be Greater Than Zero (0) ! ")
                    continue
                return value
            except ValueError:
                print("Enter A Valid Number!")

def get_non_empty_string(massage):
        while True:
            try:
                value=input(massage).strip()
                if value==" ":
                    print("Values Can't Be Empty!")
                    continue
                return value
            except ValueError:
                print("Enter A Valid Input!")