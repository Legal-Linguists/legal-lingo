import { Component, OnInit,ViewChild,ElementRef } from '@angular/core';

@Component({
  selector: 'app-choose-document',
  templateUrl: './choose-document.component.html',
  styleUrls: ['./choose-document.component.css']
})
export class ChooseDocumentComponent implements OnInit {

  constructor() {
   }
  
  continue(){
    window.location.href = "viewdocument"
  }
  uploadDoc(){
    
  }
  ngOnInit(): void {
  }

}
