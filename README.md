## Django project Set-up :

###   Python virtual environment setup
```
python -m venv env
env\Scripts\activate   # for Windows
# if u face any error , u have to set policy just chatGPT it :)
```
###   Clone my repo
```
git clone <my-https-url>
```
###   Djanog setup and installation
```
pip install django==4.1.13
pip install djongo==1.3.6
pip install pymongo==3.12.3
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install djangorestframework-simplejwt==5.3.1
pip install boto3==1.33.13
pip install django-extensions==3.2.3

```

###   MongoDB setup in docker
```
# Open new terminal
# To run mongodb in docker container
docker run -d
--name container_name
-e MONGO_INITDB_ROOT_USERNAME=username
-e MONGO_INITDB_ROOT_PASSWORD=password
-e MONGO_INITDB_DATABASE=DB_name
-p 27017:27017
xxx
#replace xxx with image id of the mongodb pulled
```
###  Run migrations
```
# Ensure that ur in the dir where manage.py exists
python manage.py makemigrations
python manage.py migrate
```
### Start server
```
python manage.py runserver
```
## Backend Design
![Alt text](https://github.com/Hareessh-P/CodeCrafter/blob/master/design-images/instructor_pov_design.jpeg)


# Chess Engine Model Architecture

```mermaid
graph TD
  A[Board Representation] --> B[Utilize bitboards for an efficient representation of the chessboard]
  B --> C[With each piece type having a separate bitboard]
  A --> D[Move Generation]
  D --> E[Implement algorithms for generating legal moves]
  E --> F[Based on the current board state]
  A --> G[Evaluation Function]
  G --> H[Develop an evaluation function]
  H --> I[Assesses the desirability of a given board position]
  I --> J[Consider factors like piece values, positional advantages, and potential threats]
  A --> K[Search Algorithm]
  K --> L[Implement the minimax algorithm with alpha-beta pruning]
  L --> M[Integrate iterative deepening to gradually increase the search depth]
  A --> N[Optimization Techniques]
  N --> O[Integrate various optimization techniques]
  O --> P[Including transposition tables, quiescence search, move ordering]
  O --> Q[Parallel search, null move pruning, late move reduction]
  Q --> R[Futility pruning, and the killer heuristic]
  A --> S[User Interface (Optional)]
  S --> T[Include a user interface to allow human interaction]
  T --> U[Displaying the board and moves]
```

