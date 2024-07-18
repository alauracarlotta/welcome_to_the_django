"""
IMPORT > proga.py / progb.py
¹ NOTE =>
    nota em lesson_02 file
"""

print('begin', __name__)
import proga

print('Define fb')
def fb():
    print('dentro fb')
    proga.fa()

print('chama fb')
fb()

print('end', __name__) # NOTE¹
