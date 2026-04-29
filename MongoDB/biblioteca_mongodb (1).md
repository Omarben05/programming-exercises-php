CREARE DATABASE A SUPPORTO DI APPLICAZIONE BIBLIOTECA 

1. installare mongodb  
   [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)  
     
2. effettuare sign in , aprire mongodb atlas su google e creare una connection, che si deve riaprire in mongodb compass  
     
3. aprire la shell e creare un database con il comando “use”   es. use biblioteca  
     
4. creare 4 collections : db.createCollection(“”)   all’interno degli apici : books, authors, borrowers e loans  
     
5. riempire le collections facendo un insert oppure cliccando add ed inserendo file csv o json.    
6. 

esempi:   
db.””.insertOne({  
}

per vedere tutti:     
db.””.find()

per vedere nello specifico :  
db.””.find(   
{  
parametro: valore   
})

db.authors.insertOne({  
  \_id: 1,  
  name: "George Orwell",  
  birth\_year: 1903,  
  nationality: "British"  
})

db.authors.find(   
{

**\_id**: 1

**name**: "George Orwell"

**birth\_year**: 1903

**nationality**: "British"  
})

script: 

use biblioteca;

// Creazione collection authors  
db.createCollection("authors");  
db.authors.createIndex({ \_id: 1 }); // \_id è implicito, ma indicizzo comunque

// Creazione collection books  
db.createCollection("books");  
db.books.createIndex({ \_id: 1 });

// Creazione collection borrowers  
db.createCollection("borrowers");  
db.borrowers.createIndex({ \_id: 1 });

// Creazione collection loans  
db.createCollection("loans");  
db.loans.createIndex({ \_id: 1 });

// Esempio di inserimento documenti con struttura richiesta  
db.authors.insertOne({  
  \_id: 1,  
  name: "Italo Calvino",  
  birth\_year: 1923,  
  nationality: "Italian"  
});

db.books.insertOne({  
  \_id: 1,  
  title: "Il barone rampante",  
  author\_id: 1,  
  genre: "Romanzo",  
  published\_year: 1957  
});

db.borrowers.insertOne({  
  \_id: 1,  
  name: "Mario Rossi",  
  email: "mario.rossi@email.it"  
});

db.loans.insertOne({  
  \_id: 1,  
  book\_id: 1,  
  borrower\_id: 1,  
  loan\_date: new Date("2025-06-23")  
});

