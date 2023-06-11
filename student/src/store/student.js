import $ from 'jquery';

const ModuleStudent = {
    namespaced: true,
    state: {
        id: '',
        username: '',
        photo: '',
        is_login: false,
        college: '',
        date_of_birth: '',
        gender: '',
        student_type: '',
        bio: '',
        email: '',
        phone: '',
        is_selected: false,
        select_limit: 0,
        select_count: 0,
        tutor_id: '',
        tutor: '',
        user: ''
  },
  getters: {
  },
  mutations: {
        updateStudent(state, student) {
            state.id = student.id;
            state.username = student.username;
            state.photo = student.photo;
            state.college = student.college;
            state.date_of_birth = student.date_of_birth;
            state.gender = student.gender;
            state.student_type = student.student_type;
            state.bio = student.bio;
            state.email = student.email;
            state.phone = student.phone;
            state.is_selected = student.is_selected;
            state.select_limit =  student.select_limit;
            state.select_count = student.select_count;
            state.tutor = student.tutor;
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
            state.is_login = false;
            state.user = '';
      }
  },
  actions: {
        get_info(context) {
            context.state.is_login = true;
            $.ajax({
                url: 'http://8.130.65.99:8002/student/get_info/',
                type: 'GET',
                data: {
                    user: context.state.user,
                },
                success(resp) {
                    if (resp.result === 'success') {
                        context.commit('updateStudent', resp.date);
                    }
                }
            })
        },
      logout(context) {
            context.commit('logout')
      }
  },
  modules: {
  }
};
export default ModuleStudent;