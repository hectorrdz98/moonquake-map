<p style="text-align: center;
    font-size: 32px;
    font-weight: 700;
    background: -webkit-linear-gradient(-70deg, #52B69A 0%, #B5E48C 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -webkit-box-decoration-break: clone">
    Moonquake Map 🦆
</p>

## HIGH-LEVEL PROJECT SUMMARY

We developed a web application that shows it's users events that were registered by Apollo Mission's instruments which include moonquakes and artificial impacts. These events are shown to the users in an interactive way, were they can explore the different locations were moonquakes happened. They have access to some filters that return relevant information displayed on the screen about the event they selected. This tool can help understand a part of the history of the moon.

Created by 
- [Héctor Daniel Rodríguez Feregrino](https://github.com/hectorrdz98)
- [Jesica Marlen Roque Moreno](https://github.com/Jesicaroque)
- [José Antonio Juarez Trujillo](https://github.com/AntonioJuarezDev)
- [André Jerónimo López Nápoles](https://github.com/Candre29)

Link to the final project: [https://github.com/hectorrdz98/moonquake-map](https://github.com/hectorrdz98/moonquake-map)

Link to the demo of the project: [https://youtu.be/qzmVYdUcmsc](https://youtu.be/qzmVYdUcmsc)

Link to a live demo of the project: [https://moonquake-map-front-end.vercel.app](https://moonquake-map-front-end.vercel.app)

## DETAILED PROJECT DESCRIPTION

We created a project divided in two parts, the front-end with was developed using VueJS (Javascript framework), ThreeJS (node library) and ThreeGlobe (which if a module for ThreeJS), and the back-end with was developed using FastAPI (Python framework) and for the database we used SQLite for it's simplity and ease of use, here we store the data we collected from the .csv files provided from the NASA Archive.

The web application renders a canvas with includes:
- The moon element.
- The moon surface.
- The moonquakes represented as lines on the moon surface, the height and color of these lines is given by the depth of each moonquake, the higher the depth the higher the line and the greener the color of it.

## SPACE AGENCY DATA

- We used the .csv files provided by the Nasa found in https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_seismic_event_catalog/data/ from the "Apollo Passive Seismic Experiment Expanded Event Catalog Data Collection".

- For the moon texture and displacement we used the "CGI Moon Kit" also provided by the Nasa found in https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720

- For some validations made we also used the PDF "Apollo Passive Seismic Experiment Expanded Event Catalog" found in https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_seismic_event_catalog/document/moonquake_catalog_desc.pdf

## HACKATHON JOURNEY
Our experience in the hackathon was really good, we managed to finish all the things that we proposed during the time working in this challenge. We learned how to deploy a FastAPI application into Vercel, and managed to connect it with our front-end application.

We selected the "Make a Moonquake Map!" challenge because we previously had experience with web applications, and wanted to build something interesting here. We also worked in our team communication while participating in this hackathon.

## PROJECT SETUP

This project has two separated components, an API built with Laravel and a front-end
application built with VueJS. So, there are different configurations in order to set up
the components properly and successfully run the project.

## Set up FastAPI back-end

First move to working directory "back-end".

```sh
cd back-end
```

### Installing dependencies

Install all the php dependencies using composer.

```sh
pip install -r requirements.txt
```

### Running the back-end project

Run the back-end service at the port :8000

```sh
python main.py
```

## Set up VueJS front-end

Now, to set up and run the VueJS application first you have to
access the "front-end" directory.

```sh
cd front-end
```

### Installing dependencies

Then install all the node dependencies using npm.

```sh
npm install
```

### Running the project

Now you can use npm to run the project.

```sh
npm run dev
```

## Interact with the application

Now go to the browser and enter the URL given by the ```npm run dev``` command to access the aplication.


## REFERENCES

- NASA csv files used for out back-end: https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_seismic_event_catalog/data/

- Moon texture and displacement: https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720

- Nomenclature for moonquakes: https://pds-geosciences.wustl.edu/lunar/urn-nasa-pds-apollo_seismic_event_catalog/document/moonquake_catalog_desc.pdf

- ThreeJS library: https://threejs.org

- ThreeGlobe: https://github.com/vasturiano/three-globe

- VueJS framework: https://vuejs.org

- FastAPI framework: https://fastapi.tiangolo.com

- Github version control manager: https://github.com

- Vercel deployment tool: https://vercel.com/dashboard
