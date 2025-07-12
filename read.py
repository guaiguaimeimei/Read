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
        record_list:list[Record]=[]
        for line in f.redalines():
            line=line.sterp():
            data_list=line.split(",")
            record=Record(data_list[0],data_lisr[1],imt(data_lisr[2]),data_list[3])
            record_list.append(record)
         f.close() 
        return record_list
        
