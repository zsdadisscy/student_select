// import $ from 'jquery';

const ModuleStudent = {
    state: {
        id: '',
        username: '',
        photo: '',
        is_login: false,
        college: '',
        data_of_birth: '',
        gender: '',
        student_type: '',
        bio: '',
        email: '',
        phone: '',
        is_selected: false,
        select_limit: 0,
        select_count: 0,
        tutor_id: '',
        tutor_name: '',
  },
  getters: {
  },
  mutations: {
        updateStudent(state, student) {
            state.id = student.id;
            state.username = student.username;
            state.photo = student.photo;
            state.college = student.college;
            state.data_of_birth = student.data;
            state.gender = student.gender;
            state.student_type = student.student_type;
            state.bio = student.bio;
            state.email = student.email;
            state.phone = student.phone;
            state.is_selected = student.is_selected;
            state.select_limit =  student.select_limit;
            state.select_count = student.select_count;
            state.tutor_name = student.tutor_name;
        },
      logout(state) {
            state.id = '';
            state.username = '';
            state.photo = '';
            state.college = '';
            state.data_of_birth = '';
            state.gender = '';
            state.student_type = '';
            state.bio = '';
            state.email = '';
            state.phone = '';
            state.is_selected = '';
            state.select_limit =  '';
            state.select_count = '';
            state.tutor_id = '';
            state.tutor_name = '';
      }
  },
  actions: {
        login(context, data) {

        }
  },
  modules: {
  }
};
export default ModuleStudent;