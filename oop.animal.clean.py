class Animal ():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.alive = True

    def sleep(self):
        return 'zzzzz'

    def eat(self,food):
        return 'nom nom NOM on' + food

    def potty(self):
        return  "...... .... uhhhh 0.o ---- SPLOGH!"

    def shout_own_name(self):
        return 'MY NAME IS' + self.name.upper()


