import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p>
      book-detail works!
    </p>
  `,
  styleUrls: ['./book-detail.component.css']
})
export class BookDetailComponent {

}
