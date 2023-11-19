class AcGame {
    constructor(id) {
        console.log("creat ac game");
        this.id = id;
        this.$ac_game = $('#' + id);
        this.menu = new AcGameMenu(this);
    }
}

