import os
import sys
from django.core.asgi import get_asgi_application
import uvicorn
from mangum import Mangum

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site2.settings')

# for resolving imports
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))

app = get_asgi_application()
handler = Mangum(app) # aws lambda adapter

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)