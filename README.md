# Tech Xperience Philips case

## Instructions
1. Clone repository: ```CMD: git clone https://github.com/BMark96/tech_xperience_philips.git```
2. Remove placeholder file from ```tech_xperience_philips/prediction``` and from ```tech_xperience_philips/data/test``` directories
3. Place validation images to ```tech_xperience_philips/data/test``` directory
4. Navigate to ```tech_xperience_philips``` directory and build docker image: ```CMD: sudo docker build -t philips_challenge .```
5. Run evaluation: ```CMD: sudo docker run -v <path of tech_xperience_philips directory>/prediction/:/prediction/ philips_challenge```
6. Output can be found in the following file: ```<path of tech_xperience_philips directory>/prediction/prediction.txt```
