## API Endpoints

   - **GET** `/books/`: Retrieve all books (public access).
   - **GET** `/books/<int:pk>/`: Retrieve a specific book by ID (public access).
   - **POST** `/books/create/`: Create a new book (authenticated users only).
   - **PUT** `/books/<int:pk>/update/`: Update