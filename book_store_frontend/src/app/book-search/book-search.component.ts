import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-book-search',
  standalone: true,
  imports: [CommonModule],
  template: `
  <section>
    <form>
      <input type="text" placeholder="Filter by city">
      <button class="primary" type="button">Search</button>
    </form>
  </section>
  `,
  styleUrls: ['./book-search.component.css']
})
export class BookSearchComponent {

}
