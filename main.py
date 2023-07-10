from ursina import  *
from ursina.prefabs.first_person_controller import  FirstPersonController #Esse módulo importa todo o sistema de movimento em primeira pessoa, onde temos direcionais e controle de camera com o mouse

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')

block_pic = 1
def update():
    global block_pic
    if held_keys['1']: block_pic = 1
    if held_keys['2']: block_pic = 2
    if held_keys['3']: block_pic = 3
    if held_keys['4']: block_pic = 4



class Voxel(Button):
    def __init__(self,position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5, #orientação inicial do cubo
            texture = texture,
            #texture= 'brick',
            #color = color.white,
            color= color.color(0,0,random.uniform(0.9,1)),
            #highlight_color = color.lime,
            scale = 0.5 #ajusta o tamanho dos bloos para eles não se sobreporem
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pic == 1: Voxel(position=self.position + mouse.normal, texture=grass_texture) #essa texture é para os blocos novos inseridos
                if block_pic == 2: Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pic == 3: Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pic == 4: Voxel(position=self.position + mouse.normal, texture=dirt_texture)
            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super(Sky, self).__init__(
            parent = scene,
            model = 'sphere', #para criar uma céu, criamos um fundo como uma esfera gigante
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )
#tem que ser x e z devido as direcionais 3d
for z in range(30):
    for x in range(30):
        voxel = Voxel(position = (x,0,z)) #esse for vai pegar a textura da class button (oque estiver em texture=)

player = FirstPersonController()
sky = Sky()

app.run()