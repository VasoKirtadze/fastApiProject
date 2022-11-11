from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base


class Games(Base):
    __tablename__ = "Games"

    id = Column(Integer, primary_key=True)

    position_1 = Column(String, default=None)
    position_2 = Column(String, default=None)
    position_3 = Column(String, default=None)
    position_4 = Column(String, default=None)
    position_5 = Column(String, default=None)
    position_6 = Column(String, default=None)
    position_7 = Column(String, default=None)
    position_8 = Column(String, default=None)
    position_9 = Column(String, default=None)

    winner = Column(String, default=None)
    finished = Column(Boolean, default=False)

    move_counter = Column(Integer, default=0)

    last_entry = Column(String)

    def define_position(self, num, value):
        if num == 0:

            if self.position_1 != None:
                return False
            else:

                self.position_1 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 1:
            if self.position_2 is not None:
                return False
            else:
                self.position_2 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 2:
            if self.position_3 is not None:
                return False
            else:
                self.position_3 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 3:
            if self.position_4 is not None:
                return False
            else:
                self.position_4 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 4:
            if self.position_5 is not None:
                return False
            else:
                self.position_5 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 5:
            if self.position_6 is not None:
                return False
            else:
                self.position_6 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 6:
            if self.position_7 is not None:
                return False
            else:
                self.position_7 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 7:
            if self.position_8 is not None:
                return False
            else:
                self.position_8 = value
                self.move_counter += 1
                self.last_entry = value
                return True
        if num == 8:
            if self.position_9 is not None:
                return False
            else:
                self.position_9 = value
                self.move_counter += 1
                self.last_entry = value
                return True

    def state(self):
        if self.move_counter >= 5:
            if self.position_1 is not None and self.position_1 == self.position_2 == self.position_3 or \
                    self.position_1 is not None and self.position_1 == self.position_4 == self.position_7 or \
                    self.position_1 is not None and self.position_1 == self.position_5 == self.position_9 or \
                    self.position_2 is not None and self.position_2 == self.position_5 == self.posiiton_8 or \
                    self.position_3 is not None and self.position_3 == self.position_6 == self.position_9 or \
                    self.position_3 is not None and self.position_3 == self.position_5 == self.position_7 or \
                    self.position_4 is not None and self.position_4 == self.position_5 == self.position_6 or \
                    self.position_7 is not None and self.position_7 == self.position_8 == self.position_9:
                self.winner = self.last_entry
                self.finished = True
            elif self.move_counter >= 5 and self.move_counter == 9:
                self.winner = 'null'
                self.finished = True



class History(Base):
    __tablename__ = 'History'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('Games.id'))
    position = Column(Integer)
    type = Column(String)
