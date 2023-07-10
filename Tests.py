'''

from ursina import  *

def update():
    if held_keys['a']:
        #Os argumentos .x e .y definirão a orientação do objeto, vertical ou horizontal
        square.rotation = Vec3(0, 0, -90)
        square.x -= 10 * time.dt
        square.rotation = Vec3(0,0,-90)
    if held_keys['d']:
        square.rotation = Vec3(0, 0, 90)
        square.x += 10 * time.dt
    if held_keys['w']:
        square.rotation = Vec3(0, 0, 0)
        square.y += 10 * time.dt
    if held_keys['s']:
        square.rotation = Vec3(0, 0, 180)
        square.y -= 10 * time.dt

app = Ursina()

#test_square = Entity(model = 'quad', color = color.blue, scale = (2,2), position = (5,3))
test_square = load_texture('assets/nave.png')
square = Entity(model = 'quad',texture = test_square)
#nav_texture = load_texture('assets/nave.png')
#nav = Entity(model = 'quad', texture = nav_texture)

app.run()
'''

from ursina import  *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube', #Formato de cudo é diferente de quadrado, o cubo tem a dimentção 3d e pode ser visualizado nas rotações x,y,z
            color = color.white,
            texture = 'white_cube', # textura branca vai mostrar as marcações e divisas do cubo
            rotation = Vec3(45,45,45)
        )

class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene, # tornar a imagem como fundo
            model = 'cube',
            texture = 'brick',
            color = color.red,
            highlight_color = color.brown, #mudar a cor quando passar o mouse por cima
            press_color = color.lime #mudar de cor ao clicar
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down': #se o botão esquedo do mouse for acionado
                print('botom press')
'''
def update():
    if held_keys['a']:
        #Os argumentos .x e .y definirão a orientação do objeto, vertical ou horizontal
        test_square.x -= 10 * time.dt
'''
app = Ursina()

#test_square = Entity(model = 'quad', color = color.blue, scale = (2,2), position = (5,3))
#hand_texture = load_texture('assets/fundo.png')
#hand = Entity(model = 'quad',texture = hand_texture)

testing_cube = Test_button()

app.run()



#Com apenas as linhas abaixo, já conseguimos criar o básico do mundo graças as funções da biblioteca
'''
from ursina import  *
from ursina.prefabs.first_person_controller import  FirstPersonController #Esse módulo importa todo o sistema de movimento em primeira pessoa, onde temos direcionais e controle de camera com o mouse

class Voxel(Button):
    def __init__(self,position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5, #orientação inicial do cubo
            #texture = 'white_cube',
            texture= 'brick',
            color = color.red,
            highlight_color = color.brown
        )

app = Ursina()

for z in range(8):
    for x in range(8):
        vx = Voxel(position = (x,0,z))

player = FirstPersonController()

app.run()
'''