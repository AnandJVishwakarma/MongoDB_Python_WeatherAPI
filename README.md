# Steps to run the project

- Step 1: Install packages using requirements.txt file
- Step 2: Set API key generated from Open Weather API (https://openweathermap.org/api)
- Step 3: Set MongoDB database using "docker volume create mongodb_database && docker-compose up -d"
- Step 4: Load Weather data using "python weather_data_collector"  and enter location name such as "Mumbai" (Iterate same process for adding more records for other locations)
- Step 5: Enable CLI to access data from mongodb database using "python CLI_interface"

EOF
