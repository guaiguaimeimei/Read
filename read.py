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
class JsonFilereader(Filereader):
    def __init__(self,path):
        self.puth=path
        
    def read_date(self->list[Record]:
        f=open(self.path,"r",encoding="UTF-8")
        record_list:list[Record]=[]
        for line in f.redalines():
            data_dict=json.loads(line)
            record=Record(data_dict["date"],data_dict["order_id"],int(data_dice["amount"]),data_dict["city"])
            record_list.append(record)
         f.close() 
        return record_list
