import pandas as pd
from .models import Recruitment


def main():
    df = pd.read_csv('student-info.csv')
    # print(df['Student Name'][0])

    for i in range(len(df)):
        # print(df['Student ID'][i],df['Student Name'][i],df['Email'][i],df['Section'][i])
        id = df['id'][i]
        name = df['name'][i]
        email = df['id'][i] + '@uap-bd.edu'
        phone = df['phone'][i]
        address = df['address'][i]
        blood = df['blood'][i]
        section = ''
        if int(id) < 20101060:
            section = 'A'
        else:
            section = 'B'
        student = Recruitment(id=id,
                              name=name,
                              email=email,
                              phone=phone,
                              address=address,
                              blood_group=blood,
                              section=section
                              )
        student.save()


if __name__ == '__main__':
    main()
