import { isNonNullChain } from "typescript";

export default class SearchFilter {
  place: string | null;
  startDate: string | null;
  endDate: string | null;
  location: string | null;
  price: number | null;
  days: number | null;

  constructor(place: string | null = null, startDate: string | null = null, endDate: string | null = null, location: string | null = null, price: number | null = null, days: number | null = null) {
    this.place = place;
    this.startDate = startDate;
    this.endDate = endDate;
    this.location = location;
    this.price = price;
    this.days = days;
  }

}