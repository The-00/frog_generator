from frog import Frog
from PIL import Image
import io
import base64

frogsize = 400

frog = Frog(goodeyes=True)
frogim = frog.get(frogsize)

byte_io = io.BytesIO()
frogim.save(byte_io, 'PNG')
binary_frog = byte_io.getvalue()
base64_frog = base64.b64encode(binary_frog)

print(str(base64_frog).split("'")[1])

