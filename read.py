from data import Record
class Filereader: 
    def read_date(self->list[Record]:
        pass
class TextFilereader(Filereader):
    def __init__(self,path):
        #定义文件路径
        self.path=path
    #实现父类
    def read_date(self->list[Record]:
        f=open(self.path,"r",encoding="UTF-8")
        for line in f.redalines():
            line=line.sterp():
            line.split(",")
