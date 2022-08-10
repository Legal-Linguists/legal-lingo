import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Legal-Lingo-Website-v2';
  firstView = true;
  secondView = false;
  home(){
    this.firstView = true;
    this.secondView = false;
  }
  goToUploadDocument(){
    this.firstView = false;
    this.secondView = true;
  }
  
  continue(){

  }
}

