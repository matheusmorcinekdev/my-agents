function getRandomQuote() {
    const quotes = [
        '"All we have to decide is what to do with the time that is given us." - Gandalf',
        '"Even the smallest person can change the course of the future." - Galadriel',
        '"There is some good in this world, and it\'s worth fighting for." - Samwise Gamgee',
        '"I wish it need not have happened in my time." - Frodo Baggins',
        '"Not all those who wander are lost." - Bilbo Baggins'
    ];
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}

console.log(getRandomQuote()); 