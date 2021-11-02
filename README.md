## Presentation

* For the summarization API coding challenge I used FastAPI framework and Transformers library from HuggingFace for summarization task

## Requirements

* Install Python 3.7

* Install the required packages with: pip install -r requirements.txt

* Setup a PostgreSQL server and modify DB configuration in the database.py file situated in "core" folder

* You are set and can now start using the APP!

## How to use the APP?

* Start the app with: uvicorn main:app

* Create the first document, example request:
  POST {app_url}/documents
  BODY:
   {
     "text": "Electricity is the set of physical phenomena associated with the presence and motion of matter that has a property of electric charge. Electricity is related to magnetism, both being part of the phenomenon of electromagnetism, as described by Maxwell's equations. Various common phenomena are related to electricity, including lightning, static electricity, electric heating, electric discharges and many others. The presence of an electric charge, which can be either positive or negative, produces an electric field. The movement of electric charges is an electric current and produces a magnetic field. When a charge is placed in a location with a non-zero electric field, a force will act on it. The magnitude of this force is given by Coulomb's law. If the charge moves, the electric field would be doing work on the electric charge. Thus we can speak of electric potential at a certain point in space, which is equal to the work done by an external agent in carrying a unit of positive charge from an arbitrarily chosen reference point to that point without any acceleration and is typically measured in volts. Electricity is at the heart of many modern technologies, being used for: Electric power where electric current is used to energise equipment; Electronics which deals with electrical circuits that involve active electrical components such as vacuum tubes, transistors, diodes and integrated circuits, and associated passive interconnection technologies.Electrical phenomena have been studied since antiquity, though progress in theoretical understanding remained slow until the seventeenth and eighteenth centuries. The theory of electromagnetism was developed in the 19th century, and by the end of that century electricity was being put to industrial and residential use by electrical engineers. The rapid expansion in electrical technology at this time transformed industry and society, becoming a driving force for the Second Industrial Revolution. Electricity's extraordinary versatility means it can be put to an almost limitless set of applications which include transport, heating, lighting, communications, and computation. Electrical power is now the backbone of modern industrial society."
   }

* Check the presence of the document with:
  GET {app_url}/documents or GET {app_url}/documents/{id}

* Try the summarization end_point with:
  GET {app_url}/documents/summarize/{id}

The first time you will use the summarization end_point, it will download locally the model (here by default the Bart model is used) and may take some time.

## How to run the tests?

* Run the test suite with: pytest

## Future ?

* The app is not completed and can be improved:
  - Setup migrations for database schema modifications
  - Improve the speed of summarization end_point
  - Review the repository structure to scale with other models
  - Choose summarization model for specific needs
  - ...


Author: Pascal LIM
Contact: lim.pascal93@gmail.com
