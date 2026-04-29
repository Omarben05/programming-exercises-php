// Benagoub Omar
// SWD - Final Project - NoSQL Database Dump


// CREAZIONE DATABASE 
use foodDeliveryDB

// INSERIMENTO DATI NELLA COLLECTION 'dishes'
db.dishes.insertMany([
  {
    name: "Margherita Pizza",
    description: "Classic pizza with tomato, mozzarella and basil",
    price: 9.5,
    category: "main",
    prepTime: 15,
    calories: 800
  },
  {
    name: "Lasagna alla Bolognese",
    description: "Pasta with meat ragù and béchamel sauce",
    price: 13,
    category: "main",
    prepTime: 25,
    calories: 950
  },
  {
    name: "Tiramisu",
    description: "Traditional coffee-flavored dessert",
    price: 6,
    category: "dessert",
    prepTime: 10,
    calories: 450
  },
  {
    name: "Risotto alla Milanese",
    description: "Creamy risotto with saffron",
    price: 12,
    category: "main",
    prepTime: 20,
    calories: 700
  },
  {
    name: "Spaghetti Carbonara",
    description: "Pasta with egg, pecorino, and pancetta",
    price: 11.5,
    category: "main",
    prepTime: 18,
    calories: 820
  },
  {
    name: "Bruschetta al Pomodoro",
    description: "Grilled bread with tomato and basil",
    price: 5,
    category: "starter",
    prepTime: 5,
    calories: 200
  },
  {
    name: "Polenta con Funghi",
    description: "Polenta with sautéed mushrooms",
    price: 10,
    category: "main",
    prepTime: 22,
    calories: 600
  },
  {
    name: "Panna Cotta",
    description: "Cream pudding with berry sauce",
    price: 5.5,
    category: "dessert",
    prepTime: 10,
    calories: 350
  },
  {
    name: "Arancini Siciliani",
    description: "Fried rice balls with ragù and peas",
    price: 7,
    category: "starter",
    prepTime: 15,
    calories: 500
  },
  {
    name: "Frittura di Calamari",
    description: "Fried squid rings with lemon",
    price: 12.5,
    category: "main",
    prepTime: 15,
    calories: 650
  }
])

// INSERIMENTO DATI NELLA COLLECTION customers - con indirizzi multipli embedded
db.customers.insertMany([
  {
    firstName: "Maria",
    lastName: "Rossi",
    email: "maria.rossi@example.com",
    registrationDate: ISODate("2024-06-01T00:00:00Z"),
    addresses: [
      { street: "Via Roma 1", city: "Torino", zip: "10100", interior: "A" }
    ]
  },
  {
    firstName: "Luca",
    lastName: "Bianchi",
    email: "luca.bianchi@example.com",
    registrationDate: ISODate("2024-05-10T00:00:00Z"),
    addresses: [
      { street: "Corso Francia 45", city: "Torino", zip: "10138" }
    ]
  },
  {
    firstName: "Giulia",
    lastName: "Verdi",
    email: "giulia.verdi@example.com",
    registrationDate: ISODate("2024-07-01T00:00:00Z"),
    addresses: [
      { street: "Via Nizza 78", city: "Torino", zip: "10126" },
      { street: "Via Po 21", city: "Torino", zip: "10124", interior: "3B" }
    ]
  },
  {
    firstName: "Marco",
    lastName: "Ferrari",
    email: "marco.ferrari@example.com",
    registrationDate: ISODate("2024-06-15T00:00:00Z"),
    addresses: [
      { street: "Via Garibaldi 5", city: "Torino", zip: "10122" }
    ]
  },
  {
    firstName: "Elena",
    lastName: "Conti",
    email: "elena.conti@example.com",
    registrationDate: ISODate("2024-05-25T00:00:00Z"),
    addresses: [
      { street: "Via Genova 12", city: "Torino", zip: "10126" }
    ]
  }
])

// --- Recupero ID per riferimenti ---
const maria = db.customers.findOne({ email: "maria.rossi@example.com" })
const giulia = db.customers.findOne({ email: "giulia.verdi@example.com" })
const dish1 = db.dishes.findOne({ name: "Margherita Pizza" })
const dish2 = db.dishes.findOne({ name: "Tiramisu" })
const dish3 = db.dishes.findOne({ name: "Spaghetti Carbonara" })

// INSERIMENTO DATI NELLA COLLECTION ordini con embedded items (piatti ordinati con quantità e prezzo snapshot)
db.orders.insertMany([
  {
    customerId: maria._id,
    createdAt: ISODate("2024-06-20T12:00:00Z"),
    status: "completed",
    items: [
      { dishId: dish1._id, quantity: 2, price: 9.5 },
      { dishId: dish2._id, quantity: 1, price: 6.0 }
    ]
  },
  {
    customerId: giulia._id,
    createdAt: ISODate("2024-06-25T19:00:00Z"),
    status: "delivering",
    items: [
      { dishId: dish3._id, quantity: 1, price: 11.5 }
    ]
  },
  {
    customerId: maria._id,
    createdAt: ISODate("2024-06-30T13:30:00Z"),
    status: "preparing",
    items: [
      { dishId: dish2._id, quantity: 2, price: 6.0 }
    ]
  }
])



// Q1: Trova tutti i piatti con un prezzo superiore a 15€
db.dishes.find({ price: { $gt: 15 } }) 
// Operatore: $gt - filtra i documenti con price maggiore di 15

// Q2: Elenca gli ordini effettuati da un cliente dato il suo email
const customer = db.customers.findOne({ email: "maria.rossi@example.com" })
db.orders.find({ customerId: customer._id })
// Operatori: findOne per trovare il cliente, find per cercare ordini con customerId

// Q3: Aggiorna lo stato di un ordine a "completed"
db.orders.updateOne(
  { _id: ObjectId("64df6c2f9a1b3c5f1d123456") }, // esempio _id reale
  { $set: { status: "completed" } }
)
// Operatore: $set modifica il campo status dell’ordine

// Q4: Trova i clienti che hanno effettuato almeno 2 ordini
db.orders.aggregate([
  { $group: { _id: "$customerId", count: { $sum: 1 } } }, // raggruppa per customerId e conta
  { $match: { count: { $gte: 2 } } },                     // filtra clienti con almeno 2 ordini
  { $lookup: {                                           // unisce con la collezione customers
      from: "customers",
      localField: "_id",
      foreignField: "_id",
      as: "customer"
    }
  },
  { $unwind: "$customer" },                              // estrae il singolo cliente dall'array
  { $project: { _id: 0, email: "$customer.email", orders: "$count" } } // proietta email e numero ordini
])
// Operatori: $group (raggruppa), $match (filtra), $lookup (join), $unwind (espande array), $project (seleziona campi)

// Q5: Trova il piatto più ordinato in un intervallo di date (es. dal 2024-06-01 al 2024-06-30)
db.orders.aggregate([
  { $match: { createdAt: { $gte: ISODate("2024-06-01T00:00:00Z"), $lte: ISODate("2024-06-30T23:59:59Z") } } }, // filtra per data
  { $unwind: "$items" },                                  // espande gli elementi ordinati
  { $group: { _id: "$items.dishId", totalQuantity: { $sum: "$items.quantity" } } }, // somma quantità per piatto
  { $sort: { totalQuantity: -1 } },                      // ordina per quantità decrescente
  { $limit: 1 },                                         // prendi il primo (più ordinato)
  { $lookup: {                                          // join per mostrare info piatto
      from: "dishes",
      localField: "_id",
      foreignField: "_id",
      as: "dish"
    }
  },
  { $unwind: "$dish" },                                  // estrae il piatto dall'array
  { $project: { _id: 1, totalQuantity: 1, dishName: "$dish.name" } } // proietta risultati finali
])
// Operatori: $match (filtro data), $unwind (espande array), $group (raggruppa), $sort (ordina), $limit (limita), $lookup (join), $project (proiezione)
