pipeline {
agent any
stages {
stage(&#39;Clone Repository&#39;) {

steps {
git &#39;https://github.com/your-username/your-repo.git&#39;
}
}
stage(&#39;Build&#39;) {
steps {
sh &#39;echo &quot;Building the application...&quot;&#39;
}
}
stage(&#39;Test&#39;) {
steps {
sh &#39;echo &quot;Running tests...&quot;&#39;
}
}
stage(&#39;Deploy&#39;) {
steps {
sh &#39;echo &quot;Deploying application...&quot;&#39;
}
}
}
}
