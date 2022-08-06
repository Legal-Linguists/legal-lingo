import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-choose-functionality',
  templateUrl: './choose-functionality.component.html',
  styleUrls: ['./choose-functionality.component.css']
})
export class ChooseFunctionalityComponent implements OnInit {

  constructor() { }
  goToTranslate(){
    window.location.href = "selectdocument"
  }
  ngOnInit(): void {
  }

}
