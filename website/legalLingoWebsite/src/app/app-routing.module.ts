import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { UploadDocumentComponent } from './upload-document/upload-document.component';
import { ViewDocumentComponent } from './view-document/view-document.component';
import { ViewTranslationComponent } from './view-translation/view-translation.component';

const routes: Routes = [
  {path: "view-translation",
   component: ViewTranslationComponent},
  {
    path:'view-document',
    component: ViewDocumentComponent
  },
  {
    path:'upload-document',
    component:UploadDocumentComponent
  },
  {
    path:'**',
    component:LandingPageComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
