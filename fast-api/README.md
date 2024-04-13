## FASTAPI Setup

due to the development environment should on top docker
we should build the image first
```bash
docker build -t fastapi .
```

add ```.env```  file

details from your supabase project settings > API
https://app.supabase.com/project/_/settings/api

```txt
SUPABASE_URL=your-project-url
SUPABASE_KEY=your-anon-key
```

run the backend 
```bash
docker run -d --name fastapi --env-file ./.env -v $(pwd):/code -p 3001:80 fastapi
```

the backend ready at (http://localhost:3001)
now you can freely update the code and it auto reload


