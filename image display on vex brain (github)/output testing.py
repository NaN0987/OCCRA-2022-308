from PIL import Image
import math

#this file is a testing file that emulates how the vex will display the image on a file labeled '308output.bmp'. to test an image, set pixel_grid to the tuple of image data



im = Image.new('RGBA',(480,240))

pixelGrid = ((('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),
(('#000000',61),),(('#000000',61),),(('#af4124',1),('#8e331a',4),('#a55d4a',1),('#af4124',1),('#a55d4a',2),('#6c4938',1),('#a55d4a',4),('#a2918d',1),('#6c4938',1),('#a2918d',1),('#6c4938',1),('#db7956',4),('#3f241b',1),('#db7956',1),('#6c4938',1),('#db7956',1),('#6c4938',1),('#db7956',1),('#a55d4a',7),('#db7956',1),('#a55d4a',10),('#af4124',1),('#a55d4a',1),('#8e331a',1),('#af4124',4),('#8e331a',1),('#af4124',1),('#8e331a',6)),
(('#6c4938',1),('#a55d4a',1),('#a2918d',1),('#a55d4a',3),('#af4124',2),('#a55d4a',6),('#a2918d',4),('#db7956',1),('#a55d4a',1),('#db7956',1),('#6c4938',1),('#3f241b',1),('#db7956',2),('#6c4938',1),('#db7956',1),('#a55d4a',17),('#af4124',2),('#a55d4a',1),('#af4124',3),('#a55d4a',1),('#af4124',7),('#8e331a',1),('#a2918d',1),('#a55d4a',1)),
(('#af4124',1),('#a55d4a',1),('#a2918d',1),('#a55d4a',11),('#6c4938',1),('#a55d4a',1),('#a2918d',1),('#db7956',1),('#6c4938',1),('#db7956',1),('#a55d4a',2),('#3f241b',2),('#db7956',2),('#a2918d',1),('#6c4938',1),('#a55d4a',10),('#af4124',1),('#a55d4a',1),('#af4124',12),('#8e331a',2),('#af4124',3),('#8e331a',2),('#a2918d',1),('#6c4938',1)),
(('#a55d4a',14),('#a2918d',1),('#db7956',6),('#a55d4a',1),('#6c4938',1),('#3f241b',1),('#db7956',2),('#3f241b',1),('#8e331a',1),('#a55d4a',13),('#af4124',16),('#8e331a',4)),
(('#a55d4a',15),('#db7956',5),('#6c4938',2),('#3f241b',1),('#a55d4a',1),('#db7956',3),('#6c4938',1),('#a55d4a',14),('#af4124',1),('#a55d4a',3),('#af4124',3),('#a55d4a',1),('#af4124',8),('#8e331a',3)),
(('#6c4938',1),('#a55d4a',12),('#af4124',1),('#a55d4a',1),('#af4124',1),('#a55d4a',1),('#3f241b',1),('#a55d4a',1),('#6c4938',1),('#a2918d',1),('#db7956',6),('#6c4938',1),('#a55d4a',4),('#db7956',1),('#a55d4a',7),('#af4124',1),('#a55d4a',1),('#af4124',1),('#8e331a',1),('#a55d4a',1),('#af4124',4),('#8e331a',2),('#af4124',3),('#8e331a',7)),
(('#6c4938',2),('#8e331a',1),('#a55d4a',2),('#af4124',1),('#8e331a',1),('#a55d4a',6),('#af4124',2),('#a55d4a',6),('#af4124',1),('#a55d4a',15),('#af4124',1),('#a55d4a',8),('#af4124',11),('#8e331a',4)),
(('#6c4938',4),('#8e331a',2),('#a55d4a',21),('#af4124',1),('#a55d4a',13),('#af4124',1),('#a55d4a',2),('#af4124',4),('#8e331a',13)),
(('#6c4938',5),('#a55d4a',36),('#af4124',1),('#a55d4a',1),('#af4124',7),('#8e331a',11)),(('#3f241b',7),('#6c4938',3),('#a55d4a',35),('#af4124',5),('#8e331a',11)),
(('#3f241b',2),('#6c4938',45),('#3f241b',14)),(('#3f241b',4),('#6c4938',2),('#3f241b',1),('#6c4938',41),('#3f241b',13)),(('#3f241b',3),('#6c4938',2),('#3f241b',1),('#6c4938',43),('#3f241b',12)),
(('#6c4938',22),('#a55d4a',1),('#6c4938',29),('#3f241b',3),('#6c4938',1),('#3f241b',5)),(('#6c4938',50),('#3f241b',11)),(('#6c4938',2),('#a55d4a',1),('#3f241b',1),('#6c4938',1),('#a55d4a',1),('#3f241b',1),('#6c4938',1),('#a55d4a',1),('#6c4938',1),('#a55d4a',1),('#8e331a',1),('#6c4938',1),('#a55d4a',2),('#6c4938',1),('#a55d4a',3),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#3f241b',1),('#db7956',2),('#3f241b',1),('#a55d4a',2),('#a2918d',1),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#3f241b',1),('#db7956',1),('#a55d4a',1),('#3f241b',1),('#db7956',1),('#a55d4a',1),('#6c4938',1),('#a55d4a',2),('#db7956',1),('#3f241b',1),('#a55d4a',2),('#3f241b',1),('#a55d4a',2),('#6c4938',2),('#3f241b',1),('#6c4938',1),('#3f241b',1),('#6c4938',2),('#3f241b',3)),
(('#6c4938',2),('#a55d4a',1),('#3f241b',1),('#6c4938',1),('#a55d4a',1),('#3f241b',1),('#6c4938',1),('#a55d4a',1),('#6c4938',1),('#a55d4a',1),('#8e331a',1),('#6c4938',1),('#a55d4a',6),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#3f241b',1),('#a55d4a',1),('#db7956',1),('#3f241b',1),('#a55d4a',2),('#6c4938',1),('#db7956',1),('#a55d4a',2),('#3f241b',1),('#a55d4a',2),('#3f241b',1),('#a55d4a',3),('#6c4938',1),('#8e331a',1),('#db7956',1),('#3f241b',1),('#a55d4a',2),('#3f241b',1),('#db7956',1),('#af4124',1),('#a55d4a',1),('#3f241b',1),('#8e331a',1),('#a55d4a',1),('#3f241b',1),('#a55d4a',2),('#8e331a',1),('#3f241b',1),('#8e331a',1),('#af4124',1),('#3f241b',2)),
(('#6c4938',3),('#3f241b',1),('#6c4938',2),('#3f241b',1),('#6c4938',4),('#8e331a',1),('#6c4938',1),('#a55d4a',4),('#6c4938',1),('#a2918d',1),('#3f241b',1),('#a55d4a',2),('#3f241b',1),('#a55d4a',2),('#3f241b',1),('#db7956',1),('#a55d4a',5),('#3f241b',1),('#db7956',1),('#a55d4a',1),('#6c4938',2),('#a55d4a',1),('#db7956',1),('#3f241b',1),('#a55d4a',2),('#3f241b',1),('#db7956',1),('#a55d4a',2),('#3f241b',1),('#af4124',1),('#a55d4a',1),('#3f241b',1),('#a55d4a',1),('#af4124',1),('#6c4938',1),('#3f241b',1),('#a55d4a',1),('#af4124',1),('#3f241b',1),('#6c4938',1),('#8e331a',1),('#3f241b',2)),
(('#a55d4a',14),('#a2918d',6),('#db7956',1),('#a55d4a',1),('#a2918d',1),('#a55d4a',2),('#a2918d',1),('#a55d4a',7),('#6c4938',2),('#a55d4a',1),('#6c4938',2),('#a55d4a',1),('#6c4938',2),('#a55d4a',2),('#3f241b',1),('#6c4938',2),('#3f241b',1),('#6c4938',1),('#8e331a',1),('#6c4938',1),('#3f241b',1),('#8e331a',1),('#a55d4a',1),('#3f241b',1),('#6c4938',1),('#8e331a',2),('#3f241b',1),('#6c4938',1),('#3f241b',2)),
(('#6c4938',1),('#a55d4a',5),('#6c4938',1),('#a55d4a',10),('#a2918d',4),('#db7956',1),('#a55d4a',5),('#db7956',1),('#a55d4a',4),('#db7956',1),('#a55d4a',26),('#6c4938',2)),
(('#a55d4a',2),('#6c4938',2),('#a55d4a',2),('#6c4938',1),('#a55d4a',7),('#af4124',4),('#db7956',5),('#a55d4a',1),('#3f241b',1),('#db7956',1),('#af4124',1),('#db7956',3),('#a55d4a',31)),
(('#a55d4a',14),('#af4124',1),('#8e331a',1),('#db7956',2),('#af4124',1),('#db7956',4),('#3f241b',5),('#db7956',1),('#af4124',1),('#a55d4a',31)),
(('#a55d4a',5),('#6c4938',1),('#a55d4a',8),('#af4124',2),('#db7956',1),('#af4124',2),('#db7956',3),('#6c4938',2),('#3f241b',1),('#af4124',1),('#3f241b',1),('#db7956',2),('#af4124',1),('#a55d4a',26),('#8e331a',1),('#a55d4a',1),('#8e331a',1),('#af4124',1),('#a55d4a',1)),
(('#6c4938',10),('#a55d4a',4),('#af4124',1),('#db7956',1),('#8e331a',1),('#af4124',3),('#db7956',2),('#af4124',5),('#db7956',5),('#a55d4a',29)),
(('#a2918d',9),('#6c4938',1),('#a55d4a',4),('#af4124',2),('#8e331a',1),('#af4124',3),('#db7956',1),('#af4124',1),('#a55d4a',1),('#af4124',3),('#db7956',3),('#af4124',1),('#a55d4a',31)),
(('#a2918d',9),('#a55d4a',4),('#db7956',1),('#af4124',5),('#3f241b',2),('#db7956',1),('#3f241b',7),('#8e331a',1),('#a55d4a',1),('#db7956',1),('#a55d4a',29)),
(('#6c4938',11),('#a55d4a',3),('#af4124',3),('#db7956',4),('#3f241b',4),('#a55d4a',1),('#af4124',2),('#8e331a',2),('#6c4938',1),('#a55d4a',30)),
(('#3f241b',5),('#6c4938',5),('#a55d4a',4),('#af4124',1),('#6c4938',2),('#a2918d',3),('#3f241b',1),('#6c4938',1),('#af4124',2),('#db7956',1),('#6c4938',1),('#af4124',4),('#8e331a',1),('#a55d4a',8),('#db7956',1),('#a55d4a',13),('#af4124',1),('#a55d4a',7)),
(('#3f241b',5),('#6c4938',6),('#a55d4a',3),('#af4124',1),('#6c4938',2),('#a2918d',3),('#3f241b',1),('#6c4938',1),('#af4124',2),('#3f241b',1),('#8e331a',1),('#3f241b',3),('#af4124',1),('#3f241b',1),('#a55d4a',5),('#db7956',1),('#a55d4a',24)),
(('#a2918d',2),('#a55d4a',9),('#db7956',3),('#af4124',1),('#6c4938',1),('#a2918d',6),('#a55d4a',1),('#af4124',1),('#db7956',1),('#3f241b',5),('#a55d4a',31)),
(('#a55d4a',12),('#db7956',2),('#af4124',1),('#a2918d',1),('#a55d4a',2),('#6c4938',2),('#3f241b',2),('#8e331a',1),('#af4124',2),('#3f241b',1),('#db7956',1),('#6c4938',1),('#db7956',1),('#af4124',1),('#db7956',1),('#a55d4a',30)),
(('#a55d4a',11),('#db7956',1),('#a55d4a',1),('#db7956',1),('#af4124',1),('#a2918d',1),('#a55d4a',4),('#3f241b',3),('#af4124',1),('#6c4938',1),('#af4124',2),('#6c4938',1),('#db7956',1),('#af4124',2),('#a55d4a',3),('#db7956',1),('#a55d4a',26)),
(('#a55d4a',12),('#db7956',1),('#a55d4a',1),('#af4124',1),('#a55d4a',1),('#a2918d',1),('#a55d4a',3),('#6c4938',1),('#3f241b',2),('#db7956',1),('#af4124',2),('#8e331a',2),('#af4124',3),('#a55d4a',30)),
(('#a55d4a',14),('#af4124',1),('#a2918d',1),('#6c4938',1),('#a2918d',2),('#a55d4a',1),('#6c4938',1),('#a2918d',1),('#6c4938',1),('#af4124',1),('#db7956',1),('#af4124',6),('#db7956',1),('#a55d4a',29)),
(('#a55d4a',14),('#af4124',4),('#db7956',1),('#af4124',3),('#db7956',1),('#af4124',8),('#a55d4a',20),('#8e331a',1),('#a55d4a',9)),(('#a55d4a',18),('#db7956',1),('#6c4938',2),('#a55d4a',3),('#a2918d',5),('#a55d4a',8),('#db7956',1),('#a55d4a',5),('#a2918d',1),('#db7956',2),('#a55d4a',15)),
(('#a55d4a',18),('#db7956',2),('#3f241b',2),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#a55d4a',1),('#db7956',1),('#a55d4a',1),('#db7956',3),('#a55d4a',8),('#6c4938',1),('#db7956',2),('#8e331a',1),('#af4124',1),('#db7956',2),('#a55d4a',15)),
(('#a55d4a',12),('#db7956',1),('#a55d4a',2),('#db7956',1),('#a55d4a',1),('#db7956',2),('#a55d4a',6),('#db7956',1),('#a55d4a',13),('#8e331a',1),('#a2918d',1),('#db7956',2),('#a2918d',2),('#6c4938',1),('#3f241b',1),('#a55d4a',2),('#af4124',1),('#a55d4a',5),('#db7956',1),('#a55d4a',2),('#db7956',1),('#a55d4a',2)),
(('#6c4938',1),('#a55d4a',38),('#6c4938',3),('#db7956',1),('#af4124',1),('#3f241b',1),('#a55d4a',1),('#8e331a',1),('#a55d4a',8),('#6c4938',1),('#a55d4a',2),('#6c4938',3)),
(('#a55d4a',34),('#6c4938',2),('#a55d4a',1),('#6c4938',4),('#af4124',1),('#a2918d',1),('#db7956',1),('#a55d4a',1),('#8e331a',1),('#db7956',1),('#6c4938',3),('#8e331a',3),('#6c4938',3),('#8e331a',1),('#6c4938',4)),
(('#a55d4a',2),('#6c4938',2),('#a55d4a',4),('#6c4938',1),('#a55d4a',1),('#6c4938',1),('#a55d4a',1),('#6c4938',2),('#a55d4a',23),('#6c4938',1),('#a55d4a',1),('#db7956',5),('#af4124',1),('#8e331a',1),('#6c4938',3),('#a55d4a',1),('#6c4938',2),('#a55d4a',1),('#6c4938',2),('#8e331a',1),('#6c4938',5)),
(('#6c4938',2),('#a55d4a',30),('#6c4938',1),('#a55d4a',4),('#db7956',6),('#a55d4a',1),('#6c4938',9),('#8e331a',1),('#6c4938',1),('#8e331a',1),('#6c4938',1),('#8e331a',1),('#6c4938',3)),
(('#a55d4a',1),('#6c4938',1),('#a55d4a',9),('#6c4938',1),('#a55d4a',17),('#6c4938',4),('#a55d4a',1),('#db7956',7),('#a55d4a',1),('#af4124',1),('#6c4938',3),('#a55d4a',1),('#6c4938',8),('#8e331a',1),('#6c4938',1),('#8e331a',1),('#6c4938',2),('#8e331a',1)),
(('#a55d4a',1),('#6c4938',2),('#a55d4a',23),('#6c4938',1),('#a55d4a',4),('#db7956',4),('#a55d4a',1),('#af4124',1),('#db7956',4),('#af4124',1),('#6c4938',10),('#a55d4a',1),('#db7956',1),('#a55d4a',7)),
(('#6c4938',2),('#a55d4a',1),('#6c4938',1),('#a55d4a',18),('#6c4938',4),('#db7956',6),('#a55d4a',2),('#af4124',6),('#3f241b',1),('#6c4938',6),('#db7956',3),('#a55d4a',2),('#db7956',2),('#a55d4a',7)),
(('#6c4938',6),('#a55d4a',3),('#6c4938',2),('#a55d4a',4),('#6c4938',1),('#a55d4a',5),('#6c4938',3),('#db7956',5),('#a55d4a',4),('#af4124',1),('#8e331a',4),('#3f241b',8),('#6c4938',3),('#8e331a',1),('#a55d4a',1),('#db7956',3),('#a55d4a',5),('#db7956',1),('#a55d4a',1)),
(('#6c4938',15),('#3f241b',2),('#6c4938',4),('#a55d4a',1),('#3f241b',1),('#a2918d',1),('#db7956',3),('#a55d4a',1),('#8e331a',2),('#3f241b',7),('#8e331a',1),('#af4124',1),('#db7956',2),('#af4124',1),('#a55d4a',1),('#af4124',1),('#3f241b',4),('#6c4938',2),('#8e331a',1),('#a55d4a',7),('#6c4938',1),('#a55d4a',1),('#db7956',1)),
(('#6c4938',5),('#a55d4a',5),('#a2918d',5),('#3f241b',2),('#a55d4a',5),('#3f241b',1),('#db7956',8),('#af4124',1),('#8e331a',4),('#af4124',2),('#a55d4a',1),('#db7956',3),('#a55d4a',2),('#af4124',1),('#a55d4a',1),('#3f241b',2),('#a55d4a',6),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#a55d4a',2),('#8e331a',1),('#a55d4a',1)),
(('#a55d4a',2),('#a2918d',13),('#3f241b',2),('#a55d4a',5),('#3f241b',1),('#db7956',8),('#a55d4a',1),('#8e331a',1),('#af4124',2),('#a55d4a',1),('#db7956',7),('#a55d4a',1),('#af4124',1),('#6c4938',1),('#3f241b',1),('#a55d4a',1),('#8e331a',2),('#db7956',1),('#a55d4a',1),('#db7956',1),('#a55d4a',1),('#6c4938',1),('#a55d4a',1),('#db7956',2),('#6c4938',1),('#a55d4a',1),('#8e331a',1)),
(('#a2918d',15),('#3f241b',2),('#a55d4a',5),('#a2918d',1),('#db7956',8),('#a55d4a',1),('#af4124',1),('#a55d4a',1),('#af4124',1),('#db7956',6),('#a55d4a',1),('#db7956',2),('#af4124',2),('#3f241b',2),('#a55d4a',4),('#db7956',1),('#6c4938',2),('#a55d4a',3),('#6c4938',2),('#a55d4a',1)),
(('#a2918d',9),('#6c4938',1),('#3f241b',2),('#db7956',1),('#af4124',1),('#6c4938',1),('#3f241b',1),('#db7956',1),('#a55d4a',1),('#8e331a',2),('#a55d4a',2),('#db7956',9),('#a55d4a',1),('#db7956',9),('#af4124',1),('#db7956',2),('#af4124',1),('#8e331a',1),('#3f241b',2),('#a55d4a',3),('#db7956',1),('#a55d4a',1),('#6c4938',3),('#8e331a',1),('#a55d4a',2),('#6c4938',2)),
(('#a2918d',8),('#3f241b',4),('#db7956',1),('#a55d4a',2),('#3f241b',1),('#a55d4a',2),('#8e331a',2),('#af4124',1),('#db7956',1),('#a55d4a',1),('#db7956',18),('#a55d4a',1),('#db7956',2),('#a55d4a',1),('#8e331a',1),('#3f241b',2),('#6c4938',1),('#8e331a',1),('#a55d4a',1),('#db7956',1),('#6c4938',1),('#a55d4a',1),('#6c4938',3),('#3f241b',3),('#6c4938',1)),
(('#a2918d',8),('#3f241b',4),('#db7956',1),('#a55d4a',2),('#af4124',1),('#db7956',2),('#af4124',1),('#6c4938',1),('#a55d4a',1),('#8e331a',1),('#af4124',2),('#db7956',10),('#a55d4a',1),('#db7956',6),('#a55d4a',1),('#db7956',2),('#a55d4a',1),('#8e331a',1),('#3f241b',2),('#a55d4a',1),('#8e331a',1),('#a55d4a',1),('#db7956',1),('#a55d4a',1),('#6c4938',3),('#a55d4a',1),('#6c4938',1),('#8e331a',1),('#a55d4a',1),('#6c4938',1)),
(('#a2918d',7),('#6c4938',1),('#3f241b',4),('#db7956',2),('#a55d4a',1),('#3f241b',1),('#a55d4a',2),('#8e331a',1),('#3f241b',1),('#a55d4a',1),('#8e331a',1),('#3f241b',1),('#af4124',1),('#a55d4a',1),('#db7956',9),('#a55d4a',1),('#db7956',9),('#a55d4a',1),('#8e331a',1),('#3f241b',2),('#6c4938',1),('#8e331a',1),('#db7956',2),('#a55d4a',1),('#8e331a',1),('#6c4938',1),('#a55d4a',1),('#6c4938',1),('#a55d4a',2),('#6c4938',2)),
(('#a2918d',7),('#6c4938',1),('#3f241b',4),('#db7956',2),('#a55d4a',1),('#6c4938',1),('#a55d4a',1),('#db7956',1),('#8e331a',1),('#af4124',2),('#8e331a',1),('#3f241b',1),('#af4124',1),('#db7956',8),('#af4124',1),('#a55d4a',2),('#db7956',9),('#a55d4a',1),('#8e331a',1),('#3f241b',2),('#a55d4a',1),('#8e331a',1),('#db7956',3),('#a55d4a',5),('#6c4938',2),('#a55d4a',1)),
(('#a2918d',8),('#3f241b',4),('#db7956',3),('#af4124',1),('#db7956',2),('#a55d4a',1),('#af4124',4),('#a55d4a',1),('#db7956',8),('#af4124',3),('#db7956',9),('#a55d4a',1),('#8e331a',1),('#3f241b',2),('#a55d4a',1),('#db7956',4),('#af4124',1),('#db7956',1),('#a55d4a',3),('#3f241b',1),('#a55d4a',2)),
(('#a2918d',7),('#6c4938',1),('#3f241b',5),('#a55d4a',1),('#db7956',5),('#af4124',1),('#db7956',12),('#af4124',1),('#8e331a',1),('#af4124',1),('#db7956',9),('#a55d4a',1),('#3f241b',3),('#6c4938',1),('#db7956',1),('#a55d4a',2),('#db7956',1),('#a55d4a',4),('#6c4938',1),('#a55d4a',3)),
(('#3f241b',16),('#a55d4a',1),('#db7956',15),('#8e331a',3),('#af4124',1),('#db7956',8),('#af4124',1),('#3f241b',1),('#6c4938',1),('#3f241b',1),('#6c4938',1),('#a55d4a',2),('#db7956',1),('#a55d4a',9)),
(('#3f241b',15),('#8e331a',1),('#af4124',1),('#db7956',1),('#3f241b',3),('#db7956',11),('#a55d4a',1),('#af4124',2),('#8e331a',1),('#db7956',7),('#a55d4a',1),('#af4124',1),('#a2918d',1),('#3f241b',1),('#a55d4a',1),('#db7956',2),('#a55d4a',1),('#db7956',1),('#a55d4a',4),('#db7956',1),('#a55d4a',4)),
(('#3f241b',21),('#a2918d',1),('#db7956',11),('#a55d4a',1),('#af4124',1),('#8e331a',1),('#af4124',2),('#db7956',4),('#af4124',2),('#8e331a',1),('#3f241b',2),('#db7956',1),('#a55d4a',1),('#db7956',2),('#a55d4a',10)),
(('#8e331a',7),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',3),('#af4124',2),('#8e331a',4),('#af4124',1),('#8e331a',2),('#db7956',6),('#a55d4a',1),('#3f241b',1),('#af4124',4),('#8e331a',2),('#af4124',3),('#db7956',2),('#af4124',2),('#8e331a',1),('#3f241b',3),('#db7956',5),('#a55d4a',9)),
(('#af4124',3),('#8e331a',3),('#a55d4a',3),('#8e331a',5),('#af4124',1),('#8e331a',8),('#db7956',6),('#af4124',1),('#a55d4a',1),('#8e331a',1),('#3f241b',6),('#8e331a',1),('#a55d4a',2),('#af4124',1),('#8e331a',2),('#3f241b',3),('#db7956',2),('#a55d4a',2),('#db7956',6),('#a55d4a',1),('#db7956',1),('#a55d4a',2)),
(('#af4124',1),('#8e331a',6),('#af4124',4),('#8e331a',1),('#af4124',1),('#8e331a',10),('#db7956',7),('#a55d4a',2),('#af4124',3),('#8e331a',3),('#3f241b',5),('#8e331a',1),('#3f241b',1),('#6c4938',1),('#8e331a',2),('#db7956',2),('#3f241b',1),('#a55d4a',2),('#db7956',1),('#a55d4a',2),('#8e331a',5)),
(('#8e331a',7),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',6),('#af4124',2),('#8e331a',6),('#db7956',8),('#a55d4a',3),('#af4124',6),('#a55d4a',2),('#af4124',1),('#8e331a',2),('#a55d4a',1),('#8e331a',1),('#a55d4a',1),('#8e331a',12)),
(('#8e331a',6),('#af4124',1),('#8e331a',19),('#db7956',10),('#af4124',2),('#db7956',9),('#a55d4a',2),('#8e331a',12)),(('#8e331a',28),('#db7956',19),('#af4124',1),('#3f241b',1),('#8e331a',12)),
(('#8e331a',1),('#af4124',2),('#8e331a',21),('#af4124',1),('#8e331a',6),('#3f241b',1),('#8e331a',1),('#af4124',1),('#db7956',9),('#af4124',1),('#8e331a',1),('#db7956',3),('#3f241b',1),('#8e331a',12)),
(('#8e331a',7),('#af4124',2),('#8e331a',6),('#af4124',3),('#8e331a',8),('#af4124',1),('#8e331a',12),('#db7956',3),('#8e331a',1),('#af4124',1),('#8e331a',13),('#af4124',1),('#8e331a',3)),
(('#8e331a',2),('#af4124',1),('#8e331a',11),('#af4124',1),('#8e331a',3),('#af4124',2),('#8e331a',39),('#af4124',2)),(('#8e331a',1),('#af4124',7),('#8e331a',4),('#af4124',1),('#8e331a',5),('#af4124',1),('#8e331a',9),('#af4124',1),('#8e331a',20),('#af4124',1),('#8e331a',7),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',1)),
(('#8e331a',10),('#af4124',2),('#8e331a',6),('#af4124',2),('#8e331a',1),('#af4124',2),('#a55d4a',2),('#8e331a',1),('#af4124',2),('#8e331a',4),('#af4124',1),('#8e331a',13),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',9),('#af4124',1),('#8e331a',1),('#af4124',1)),
(('#8e331a',5),('#af4124',1),('#8e331a',4),('#af4124',2),('#8e331a',2),('#af4124',1),('#a55d4a',1),('#af4124',1),('#8e331a',2),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',1),('#af4124',9),('#8e331a',1),('#af4124',1),('#8e331a',2),('#af4124',3),('#8e331a',6),('#af4124',1),('#8e331a',3),('#af4124',1),('#8e331a',3),('#af4124',2),('#8e331a',2),('#af4124',2)),
(('#8e331a',2),('#af4124',4),('#8e331a',10),('#af4124',2),('#8e331a',1),('#af4124',1),('#8e331a',7),('#af4124',1),('#8e331a',4),('#af4124',1),('#8e331a',5),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',9),('#af4124',1),('#8e331a',4),('#af4124',1),('#8e331a',5)),
(('#8e331a',2),('#af4124',1),('#8e331a',5),('#af4124',1),('#8e331a',1),('#af4124',1),('#a55d4a',1),('#af4124',1),('#8e331a',3),('#af4124',5),('#8e331a',3),('#af4124',2),('#8e331a',2),('#af4124',3),('#8e331a',3),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',4),('#af4124',1),('#8e331a',4),('#af4124',2),('#8e331a',1),('#af4124',3),('#8e331a',2),('#af4124',2),('#8e331a',5)),
(('#8e331a',9),('#af4124',3),('#8e331a',2),('#a55d4a',1),('#af4124',2),('#8e331a',19),('#af4124',3),('#8e331a',1),('#af4124',4),('#8e331a',1),('#af4124',9),('#8e331a',1),('#af4124',1),('#8e331a',1),('#af4124',2),('#8e331a',1),('#af4124',1)),
(('#8e331a',8),('#3f241b',2),('#8e331a',1),('#3f241b',1),('#8e331a',11),('#3f241b',1),('#8e331a',7),('#af4124',2),('#8e331a',1),('#af4124',5),('#8e331a',1),('#af4124',20),('#8e331a',1)),
(('#8e331a',2),('#6c4938',1),('#3f241b',1),('#8e331a',4),('#3f241b',6),('#6c4938',1),('#a55d4a',1),('#a2918d',9),('#6c4938',1),('#3f241b',3),('#6c4938',1),('#8e331a',1),('#af4124',1),('#8e331a',2),('#af4124',1),('#8e331a',2),('#af4124',1),('#8e331a',1),('#af4124',13),('#8e331a',2),('#af4124',6),('#8e331a',1)),
(('#6c4938',2),('#3f241b',5),('#6c4938',1),('#a55d4a',1),('#a2918d',1),('#db7956',19),('#a2918d',1),('#8e331a',1),('#af4124',1),('#8e331a',3),('#af4124',2),('#8e331a',2),('#af4124',1),('#8e331a',1),('#af4124',2),('#8e331a',1),('#af4124',7),('#8e331a',4),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',3)),
(('#db7956',29),('#a2918d',1),('#8e331a',9),('#af4124',1),('#8e331a',1),('#af4124',1),('#8e331a',19)),(('#db7956',23),('#a55d4a',1),('#8e331a',1),('#af4124',1),('#db7956',2),('#a55d4a',1),('#a2918d',1),('#8e331a',2),('#af4124',5),('#8e331a',1),('#af4124',5),('#8e331a',4),('#af4124',1),('#8e331a',2),('#af4124',1),('#8e331a',10)),
(('#db7956',16),('#af4124',1),('#8e331a',5),('#6c4938',1),('#8e331a',1),('#6c4938',1),('#8e331a',1),('#a55d4a',1),('#db7956',1),('#a55d4a',1),('#a2918d',1),('#8e331a',1),('#3f241b',1),('#8e331a',8),('#af4124',3),('#8e331a',6),('#af4124',1),('#8e331a',10),('#af4124',1)),
(('#db7956',8),('#af4124',1),('#8e331a',2),('#3f241b',1),('#8e331a',1),('#6c4938',1),('#3f241b',15),('#a2918d',1),('#8e331a',1),('#3f241b',1),('#af4124',3),('#8e331a',1),('#af4124',1),('#8e331a',2),('#af4124',1),('#8e331a',2),('#af4124',1),('#8e331a',4),('#af4124',1),('#8e331a',3),('#af4124',2),('#8e331a',4),('#af4124',1),('#8e331a',1),('#af4124',2)),
(('#af4124',2),('#8e331a',3),('#3f241b',14),('#db7956',4),('#3f241b',1),('#8e331a',2),('#3f241b',3),('#a2918d',1),('#8e331a',1),('#3f241b',1),('#af4124',2),('#8e331a',3),('#af4124',10),('#8e331a',2),('#af4124',12)),
(('#6c4938',5),('#3f241b',1),('#8e331a',4),('#a55d4a',1),('#8e331a',3),('#a55d4a',1),('#8e331a',3),('#db7956',3),('#8e331a',1),('#a2918d',2),('#db7956',1),('#3f241b',1),('#8e331a',1),('#3f241b',2),('#a55d4a',1),('#8e331a',2),('#af4124',1),('#3f241b',1),('#af4124',1),('#8e331a',1),('#af4124',11),('#8e331a',1),('#af4124',4),('#8e331a',1),('#af4124',2),('#8e331a',1),('#af4124',2),('#8e331a',1),('#af4124',2)),
(('#a55d4a',5),('#3f241b',1),('#8e331a',1),('#a55d4a',2),('#a2918d',7),('#6c4938',2),('#3f241b',4),('#6c4938',1),('#3f241b',1),('#8e331a',7),('#af4124',2),('#6c4938',1),('#8e331a',2),('#af4124',14),('#8e331a',1),('#af4124',10)),
(('#3f241b',2),('#6c4938',3),('#8e331a',11),('#af4124',1),('#8e331a',1),('#af4124',2),('#8e331a',1),('#af4124',3),('#8e331a',8),('#af4124',1),('#6c4938',1),('#8e331a',3),('#af4124',11),('#8e331a',1),('#af4124',3),('#8e331a',1),('#af4124',1),('#8e331a',1),('#af4124',5),('#8e331a',1)),
(('#8e331a',12),('#af4124',5),('#8e331a',1),('#af4124',1),('#8e331a',1),('#af4124',12),('#3f241b',2),('#8e331a',2),('#af4124',25)),
(('#af4124',2),('#8e331a',1),('#af4124',3),('#8e331a',1),('#af4124',1),('#8e331a',3),('#af4124',2),('#8e331a',1),('#af4124',2),('#8e331a',2),('#af4124',7),('#8e331a',2),('#af4124',5),('#a2918d',1),('#3f241b',2),('#af4124',1),('#8e331a',1),('#af4124',24)),
(('#8e331a',3),('#af4124',1),('#8e331a',5),('#af4124',3),('#8e331a',1),('#af4124',20),('#8e331a',1),('#af4124',1),('#8e331a',2),('#af4124',20),('#8e331a',4)),
(('#af4124',1),('#8e331a',1),('#af4124',3),('#8e331a',1),('#af4124',24),('#8e331a',2),('#3f241b',29)),(('#af4124',12),('#8e331a',2),('#3f241b',47)),
(('#3f241b',61),),(('#3f241b',60),('#6c4938',1)),(('#3f241b',20),('#a55d4a',2),('#db7956',2),('#8e331a',1),('#3f241b',2),('#6c4938',1),('#3f241b',1),('#6c4938',32)),
(('#3f241b',4),('#6c4938',1),('#a55d4a',1),('#a2918d',10),('#3f241b',2),('#db7956',5),('#a2918d',1),('#8e331a',1),('#3f241b',1),('#6c4938',35)),
(('#a2918d',16),('#3f241b',2),('#db7956',6),('#8e331a',2),('#6c4938',35)),(('#a2918d',16),('#3f241b',2),('#db7956',6),('#8e331a',2),('#6c4938',35)),
(('#a2918d',16),('#3f241b',2),('#db7956',3),('#a55d4a',1),('#db7956',2),('#8e331a',2),('#6c4938',35)),(('#a2918d',16),('#3f241b',2),('#db7956',3),('#a55d4a',1),('#db7956',2),('#8e331a',2),('#3f241b',1),('#6c4938',34)),
(('#a2918d',16),('#3f241b',2),('#db7956',6),('#8e331a',2),('#3f241b',1),('#6c4938',32),('#a2918d',2)),(('#000000',61),),(('#000000',61),),
(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),(('#000000',61),),
)

def hexToTuple(hexString):
    return (int(hexString[1:3], 16), int(hexString[3:5], 16), int(hexString[5:], 16))

compressRatio = (4, 4)

print(len(pixelGrid))
def main():
    #screen resolution: 480x240
    x = math.floor((480 - len(pixelGrid)*compressRatio[1])/2)
    for column in pixelGrid:
        y = 0
        
        for colorLength in column:
            color = hexToTuple(colorLength[0])
        
            for i in range(0, colorLength[1]): #repeat for length of color
                for j in range(0, compressRatio[0]): #vertical compression
                    for k in range(0, compressRatio[1]): #horizontal compression
                        try:
                            im.putpixel((x+k,y+j),color)
                        except IndexError:
                            pass
                
                y += compressRatio[0]
        x += compressRatio[1]

main()

im.save("output.bmp")




