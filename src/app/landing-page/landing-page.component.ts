import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { ChooseFunctionalityComponent } from '../choose-functionality/choose-functionality.component';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.css']
})
export class LandingPageComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  goToUploadDocument(){
    
    const dialogRef = this.dialog.open(ChooseFunctionalityComponent, {
      width: '30vw',
      height: '30vw',
      data: {},
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
  ngOnInit(): void {
  }

}
