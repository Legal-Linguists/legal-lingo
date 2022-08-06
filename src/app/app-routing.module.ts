import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChooseDocumentComponent } from './choose-document/choose-document.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { ViewDocumentComponent } from './view-document/view-document.component';

const routes: Routes = [
  {path : "viewdocument",
  component: ViewDocumentComponent
  },
  {
    path: 'selectdocument',
    component : ChooseDocumentComponent
  },
  { 
    path : '**', 
    component : LandingPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
