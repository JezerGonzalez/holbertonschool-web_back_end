export default function groceriesList() {
  const groceries = new Map();

  groceries.set({ name: 'Apple', quantity: 10 });
  groceries.set({ name: 'Tomatoes', quantity: 10 });
  groceries.set({ name: 'Pasta', quantity: 1 });
  groceries.set({ name: 'Rice', quantity: 1 });
  groceries.set({ name: 'Banana', quantity: 5 });

  return groceries;
}
