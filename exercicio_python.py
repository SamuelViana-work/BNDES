import math
from datetime import date 
import datetime

def deposito(juros,vencimento):
  hoje = date.today()
  dif_meses = ((vencimento - hoje).days/30)
  total=0
  for i in range(math.floor(dif_meses)):
    total += 1000
    total *= juros
    
  return total

deposito(1.1,date(2021,12,25))