import { Component, OnInit } from '@angular/core';
import { AppConfig } from './settings';
import { BookSearchComponent } from './book-search/book-search.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    BookSearchComponent
  ],
  template: `
  <main>
    <header class="brand-name">
      <img class="brand-logo" src="/assets/logo.svg" alt="logo" aria-hidden="true">
    </header>
    <section class="content">
      <app-book-search></app-book-search>
    </section>
  </main>
`,
  styleUrls: ['./app.component.css'],
})

export class AppComponent implements OnInit{
  title = AppConfig.appName;

  ngOnInit(): void {
    // set the application title
    document.title = AppConfig.appName;
  }
}
