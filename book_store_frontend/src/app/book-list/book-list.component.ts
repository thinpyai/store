import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p>
      book-list works!
    </p>
  `,
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent {

}
