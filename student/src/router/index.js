import {createRouter, createWebHashHistory} from 'vue-router';

import LoginView from '../views/LoginView.vue'
import TutorModifyInfo from '../views/tutor/ModifyInfo.vue'
import TutorModifyPassword from '../views/tutor/ModifyPassword.vue'
import MyStudent from '../views/tutor/MyStudent.vue'
import SelectStudent from '../views/tutor/SelectStudent.vue'
import LookStudentInfo from '../views/tutor/StudentInfo.vue'
import TutorInfo from '../views/tutor/TutorInfo.vue'
import AllTutor from '../views/student/AllTutor.vue'
import StudentModifyInfo from '../views/student/ModifyInfo.vue'
import StudentModifyPassword from '../views/student/ModifyPassword.vue'
import MySelect from '../views/student/MySelect.vue'
import MyTutor from '../views/student/MyTutor.vue'
import StudentInfo from '../views/student/StudentInfo.vue'
import LookTutorInfo from '../views/student/TutorInfo.vue'
import NotFound from "../views/NotFound.vue";

const routes = [
    {
        path: '/',
        name: 'login',
        component: LoginView
    },
    {
        path: '/404/',
        name: '404',
        component: NotFound,
    },
    {
        path: '/student/modifyinfo/',
        name: 'stduent_modifyinfo',
        component: StudentModifyInfo
    },
    {
        path: '/student/modifypassword/',
        name: 'student_modifypassword',
        component: StudentModifyPassword
    },
    {
        path: '/student/alltutor/',
        name: 'alltutor',
        component: AllTutor
    },
    {
        path: '/student/myselect/',
        name: 'myselect',
        component: MySelect
    },
    {
        path: '/student/mytutor/',
        name: 'mytutor',
        component: MyTutor
    },
    {
        path: '/student/info/',
        name: 'studentinfo',
        component: StudentInfo
    },
    {
        path: '/student/tutorinfo/:tutorid/',
        name: 'looktutorinfo',
        component: LookTutorInfo
    },
    {
        path: '/tutor/modifyinfo/',
        name: 'tutor_modifyinfo',
        component: TutorModifyInfo
    },
    {
        path: '/tutor/modifypassoword/',
        name: 'tutor_modifypassoword',
        component: TutorModifyPassword
    },
    {
        path: '/tutor/mystudent/',
        name: 'mystudent',
        component: MyStudent
    },
    {
        path: '/tutor/selectStudent/',
        name: 'selectstudent',
        component: SelectStudent
    },
    {
        path: '/tutor/studentinfo/',
        name: 'lookstudentinfo',
        component: LookStudentInfo
    },
    {
        path: '/tutor/info',
        name: 'tutorinfo',
        component: TutorInfo
    },
    {
        path: '/:catchAll(.*)',
        redirect: '/404/'
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
