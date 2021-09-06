class Work:
    def __init__(self, name, owners=None):
        self.name = name
        self.owners = self.__is_valid(owners)

    def __repr__(self):
        return f'{self.name}'

    def __is_valid(self, owners):
        if owners != None:
            if isinstance(self, Paper):
                if isinstance(owners, list):
                    li = []
                    for per in owners:
                        if not isinstance(per, Researcher):
                            return f'Sorry! {per} is not a Researcher.'
                        else:
                            li.append(per)
                    return li
                else:
                    if not isinstance(owners, Researcher):
                        return f'Sorry! {owners} is not a Researcher.'
                    else:
                        return owners
            elif isinstance(self, Poetry):
                if isinstance(owners, list):
                    return 'Sorry! A poetry have only one poet.'
                else:
                    if not isinstance(owners, Poet):
                        return f'Sorry! {owners} is not a Poet.'
                    else:
                        return owners
            elif isinstance(self, Book):
                if isinstance(owners, list):
                    li = []
                    for per in owners:
                        if not isinstance(per, Writer):
                            return f'Sorry! {per} is not a Writer.'
                        else:
                            li.append(per)
                    return li
                else:
                    if not isinstance(owners, Writer):
                        return f'Sorry! {owners} is not a Writer.'
                    else:
                        return owners


class Paper(Work):
    def __init__(self, name, name_of_mag=None, year_of_pub=None, owners=None):
        self.name_of_mag = name_of_mag
        self.year_of_pub = year_of_pub
        super().__init__(name, owners)

    def num_owners(self):
        if isinstance(self.owners, list):
            return f'{self} has {len(self.owners)} researcher.'
        else:
            return f'{self} has only one researcher.'


class Poetry(Work):
    def __init__(self, name, form=None, owners=None):
        self.form = form
        super().__init__(name, owners)


class Book(Work):
    count = 0

    def __init__(self, name, ISBN, publisher=None, owners=None):
        self.ISBN = ISBN
        self.publisher = publisher
        Book.count += 1
        super().__init__(name, owners)

    def num_owners(self):
        if isinstance(self.owners, list):
            return f'{self} has {len(self.owners)} writer.'
        else:
            return f'{self} has only one writer.'

    def __del__(self):
        Book.count -= 1


class Owner:
    def __init__(self, name, email=None, gender=None):
        self.name = name
        self.email = email
        self.gender = gender

    def __repr__(self):
        return f'{self.name}'


class Researcher(Owner):
    def __init__(self, name, field, email=None, gender=None, uni=None):
        self.field = field
        self.uni = uni
        super().__init__(name, email, gender)


class Poet(Owner):
    def __init__(self, name, email=None, gender=None, style=None):
        self.style = style
        super().__init__(name, email, gender)


class Writer(Owner):
    def __init__(self, name, writer_code, email=None, gender=None, genre=None):
        self.writer_code = writer_code
        self.genre = genre
        super().__init__(name, email, gender)


Victor_Hugo = Writer('Victor Hugo', 5658)
Stephen_King = Writer('Stephen King', 4589)
Peter_Straub = Writer('Peter Straub', 8974)
Mahdi_Saeedi = Researcher('Mahdi Saeedi', 'biology')
Elias_Rahmani = Poet('Elias Rahmani')
Shahin_Alavi = Poet('Shahin Alavi')
paper1 = Paper('Vaccination of Covid-19', owners=[Mahdi_Saeedi, Victor_Hugo])
book1 = Book('The Talisman', 1234648979, owners=[Stephen_King, Peter_Straub])
book2 = Book('Les Miserables', 1545644646, owners=Victor_Hugo)
poetry1 = Poetry('Kooye Doost', owners=[Shahin_Alavi, Elias_Rahmani])
print(paper1.owners)
print(book1.owners)
print(book1.num_owners())
print(poetry1.owners)
print(Book.count)
